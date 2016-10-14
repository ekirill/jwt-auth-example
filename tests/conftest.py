# -*- coding: utf-8 -*-
import sys
import os
import datetime
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
def exp_2_weeks():
    exp = datetime.datetime.now() + datetime.timedelta(days=14)
    return int(exp.timestamp())


@pytest.fixture
def superuser_permissions():
    return ['*']


@pytest.fixture
def jwt_payload_gen(exp_2_weeks, superuser_permissions):
    def _gen_payload(sub='ekirill', exp=None, permissions=None):
        if not exp:
            exp = exp_2_weeks
        if not permissions:
            permissions = superuser_permissions

        return {
            'iss': 'ekirill.ru',
            'exp': exp,
            'permissions': permissions,
            'sub': sub,
        }

    return _gen_payload
