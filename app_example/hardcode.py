# -*- coding: utf-8 -*-
# HERE WE COLLECT EVERYTHING, THAT SHOULD EXIST IN DB OR SETTINGS CONF

# resource ids
RESOURCE_1 = 1
RESOURCE_2 = 2


USER_CREDENTIALS = {
    'ekirill': 'ekirill',
    'someuser': 'someuser',
}

SECRET_KEY = 'dsafjb3((*ASDJjkj32-0'

USER_ALLOWED_RESOURCES = {
    'ekirill': [RESOURCE_1, RESOURCE_2],
    'someuser': [RESOURCE_2],
}


AUTH_COOKIE = 'authJWT'
COOKIE_MAX_AGE = 14 * 24 * 60 * 60


def credentials_checker(login, password):
    return USER_CREDENTIALS.get(login) == password


def permissions_fetcher(login):
    return USER_ALLOWED_RESOURCES.get(login, [])
