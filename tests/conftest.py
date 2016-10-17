# -*- coding: utf-8 -*-
import sys
import os
import pytest
import json
from mock import patch


sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
))


@pytest.fixture
def secret():
    return 'someSecretString'


@pytest.fixture
def another_secret():
    return 'anotherSecretString'


@pytest.fixture
def superuser_permissions():
    return ['*']


@pytest.fixture
def jwt_payload_gen(superuser_permissions):
    def _gen_payload(sub='ekirill', permissions=None):
        if not permissions:
            permissions = superuser_permissions

        return {
            'iss': 'ekirill.ru',
            'permissions': permissions,
            'sub': sub,
        }

    return _gen_payload


@pytest.fixture
def app():
    from app_example.application import create_app
    return create_app()


@pytest.fixture
def predefined_permissions():
    return {
        'ekirill': [1, 2],
        'someuser': [2],
    }


@pytest.fixture
def permissions_fetcher(predefined_permissions):
    def _get_permissions(login):
        return predefined_permissions.get(login, [])

    return _get_permissions


@pytest.fixture
def predefined_credentials():
    return {
        'ekirill': 'ekirill',
        'someuser': 'someuser',
    }


@pytest.fixture
def credentials_checker(predefined_credentials):
    def _check_credentials(login, password):
        return predefined_credentials.get(login) == password

    return _check_credentials


@pytest.fixture
def perform_login(credentials_checker, predefined_credentials):
    def _do_login(my_client, login):
        with patch('app_example.auth.credentials_checker', credentials_checker):
            my_client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({
                    'login': login,
                    'password': predefined_credentials.get(login),
                })
            )

    return _do_login


@pytest.fixture
def perform_logout():
    def _do_login(my_client):
        my_client.get('/logout')

    return _do_login
