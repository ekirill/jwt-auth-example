# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from flask import make_response

from ekirill_auth_api.auth.api import AuthAPI, AuthError
from .hardcode import (
    SECRET_KEY, AUTH_COOKIE, COOKIE_MAX_AGE,
    credentials_checker, permissions_fetcher,
)


_auth_api = None


def get_auth_api():
    """
    :rtype: ekirill_auth_api.auth.api.AuthAPI
    """
    global _auth_api
    if _auth_api is None:
        _auth_api = AuthAPI(SECRET_KEY, credentials_checker, permissions_fetcher)

    return _auth_api


def sign_response(response, user):
    """
    Update response with authentication data
    :type response: flask.Response
    :type user: ekirill_auth.auth.user.User
    :rtype: response
    """
    api = get_auth_api()
    exp = datetime.now() + timedelta(seconds=COOKIE_MAX_AGE)
    response.set_cookie(AUTH_COOKIE, value=api.get_jwt(user), expires=exp)
    return response


def unsign_response(response):
    """
    Drop authentication data from client response
    :type response: flask.Response
    :rtype: response
    """
    exp = datetime.fromtimestamp(0)
    response.set_cookie(AUTH_COOKIE, value='', expires=exp)
    return response


def get_user(request):
    """
    :type request: flask.Request
    :rtype: ekirill_auth.auth.user.User
    """
    jwt = request.cookies.get(AUTH_COOKIE)
    if not jwt:
        return None

    api = get_auth_api()
    try:
        user = api.auth_by_jwt(jwt.encode('ascii'))
    except AuthError:
        return None

    return user


def get_access_denied_response():
    return make_response("ACCESS DENIED", 403)


def permission_required(request, resource_id):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            user = get_user(request)
            if not user or not user.is_allowed(resource_id):
                return get_access_denied_response()

            return func(*args, **kwargs)

        return wrapper
    return real_decorator
