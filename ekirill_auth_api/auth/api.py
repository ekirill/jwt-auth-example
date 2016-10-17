# -*- coding: utf-8 -*-
from ekirill_auth_api.jwt.api import JWTApi
from ekirill_auth_api.jwt.exceptions import JWTInvalidToken, JWTVerificationError

from .permissions import UserPermissions
from .user import User


class AuthError(Exception):
    pass


class AuthAPI(object):
    def __init__(self, secret_key, credentials_checker, permissions_fetcher):
        """
        :type secret_key: str
        :type credentials_checker: (str, str)->bool
        :type permissions_fetcher: (str)->list(int)
        """
        self._jwt_api = JWTApi(secret_key)
        self._credentials_checker = credentials_checker
        self._permissions_fetcher = permissions_fetcher

    def auth_by_credentials(self, login, password):
        """
        If auth is successful, User is returned. Else None is returned
        :type login: str
        :type password: str
        :rtype: ekirill_auth_api.auth.user.User
        """
        if not self._credentials_checker(login, password):
            raise AuthError('Login or password is invalid')

        allowed_resources = self._permissions_fetcher(login)

        return User(
            login=login,
            permissions=UserPermissions.from_allowed_resources(allowed_resources),
        )

    def auth_by_jwt(self, token):
        """
        :param token: bytes
        :rtype: ekirill_auth_api.auth.user.User
        """
        try:
            user_data = self._jwt_api.loads(token)
        except (JWTInvalidToken, JWTVerificationError) as e:
            raise AuthError('Token is invalid: {}'.format(e))

        if 'login' not in user_data or 'permissions' not in user_data:
            raise AuthError('Token is invalid, it has no login and premissions information')

        login = user_data['login']
        try:
            permissions = UserPermissions.from_dump(user_data['permissions'])
        except ValueError as e:
            raise AuthError('Token is invalid, it has invalid premissions: {}'.format(e))

        return User(
            login=login,
            permissions=permissions,
        )

    def get_jwt(self, user):
        """
        :type user: ekirill_auth_api.auth.user.User
        :rtype: bytes
        """
        user_data = {
            'login': user.login,
            'permissions': user.permissions.get_dump(),
        }
        return self._jwt_api.dumps(user_data)
