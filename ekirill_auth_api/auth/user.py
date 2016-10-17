# -*- coding: utf-8 -*-


class User(object):
    def __init__(self, login, permissions):
        """
        :type login: str
        :type permissions: ekirill_auth_api.auth.permissions.UserPermissions
        """
        self.login = login
        self.permissions = permissions

    def is_allowed(self, resource_id):
        return self.permissions.is_allowed(resource_id)
