# -*- coding: utf-8 -*-
from flask import request
from flask.views import MethodView

from . import OK_RESULT, FAIL_RESULT
from app_example import auth


class Login(MethodView):
    def post(self):
        login_data = request.get_json()
        login = login_data.get('login')
        password = login_data.get('password')

        api = auth.get_auth_api()
        try:
            user = api.auth_by_credentials(login, password)
        except auth.AuthError:
            resp = FAIL_RESULT(errors=['Login and/or password is invalid'])
            resp = auth.unsign_response(resp)
            return resp

        resp = OK_RESULT({'token': api.get_jwt(user).decode('ascii')})
        resp = auth.sign_response(resp, user)
        return resp


class Logout(MethodView):
    def get(self):
        resp = OK_RESULT()
        resp = auth.unsign_response(resp)
        return resp
