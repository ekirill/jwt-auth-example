# -*- coding: utf-8 -*-
from ekirill_auth_api.auth.permissions import UserPermissions


def test_permissions_dump_restore(user_permissions):
    allowed_resourses = user_permissions('ekirill')

    perms = UserPermissions.from_allowed_resources(allowed_resourses)
    assert set(allowed_resourses) == set(perms.get_allowed_resourses())

    dump = perms.get_dump()
    resored_perms = UserPermissions.from_dump(dump)
    assert set(allowed_resourses) == set(resored_perms.get_allowed_resourses())
