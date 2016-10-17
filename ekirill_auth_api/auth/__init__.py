# -*- coding: utf-8 -*-


# should be in db
USER_CREDENTIALS = {
    'ekirill': 'ekirill',
    'someuser': 'someuser',
}


# should be stored somewhere, in ENV vars for example
SECRET_KEY = 'dsafjb3((*ASDJjkj32-0'


# permission ids should be in db
RESOURCE_1 = 1
RESOURCE_2 = 2


# should be in db
USER_ALLOWED_RESOURCES = {
    'ekirill': [RESOURCE_1, RESOURCE_2],
    'someuser': [RESOURCE_2],
}
