# -*- coding: utf-8 -*-
import pytest

from ekirill_auth_api.auth.api import AuthAPI, AuthError
from ekirill_auth_api.auth.user import User


def test_auth(secret, credentials_checker, permissions_fetcher):
    auth_api = AuthAPI(secret, credentials_checker, permissions_fetcher)

    with pytest.raises(AuthError):
        user = auth_api.auth_by_credentials('ekirill', 'alsdlasjd;')

    ekirill_permissions = permissions_fetcher('ekirill')

    user = auth_api.auth_by_credentials('ekirill', 'ekirill')
    assert isinstance(user, User)
    assert set(user.permissions.get_allowed_resourses()) == set(ekirill_permissions)
    assert user.is_allowed(ekirill_permissions[0])

    token = auth_api.get_jwt(user)
    token_user = auth_api.auth_by_jwt(token)
    assert isinstance(token_user, User)
    assert set(token_user.permissions.get_allowed_resourses()) == set(ekirill_permissions)
    assert token_user.is_allowed(ekirill_permissions[0])
