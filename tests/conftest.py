# -*- coding: utf-8 -*-
import sys
import os
import pytest

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
