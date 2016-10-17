# -*- coding: utf-8 -*-
"""
Api for representing each permission as a bit in an integer number.
We consider int has only 32 bits for back compatibility
For representing resource ids more than 32, we represent list of premissions as
an array of ints. First represents 0-32, second 33-64 and so forth
"""


class UserPermissions(object):
    _allowed_resourses = None
    _dump = None

    def __init__(self, allowed_resources=None, dump=None):
        """
        :type allowed_resources: list(int)|None
        :type dump: list(int)|None
        """
        assert allowed_resources is not None or dump is not None

        if allowed_resources is not None:
            self._allowed_resourses = set(allowed_resources)

        if dump is not None:
            self._dump = dump

    @staticmethod
    def from_allowed_resources(allowed_resources):
        """
        :type allowed_resources: list(int)
        :rtype: ekirill_auth_api.auth.permissions.UserPermissions
        """
        return UserPermissions(allowed_resources=allowed_resources)

    @staticmethod
    def from_dump(dump):
        """
        :type dump: list(int)
        :rtype: ekirill_auth_api.auth.permissions.UserPermissions
        """
        if not isinstance(dump, list):
            raise ValueError('Invalid permissions dump. List is expected')
        if not all([isinstance(x, int) for x in dump]):
            raise ValueError('Invalid permissions dump. Each dump element must be an int')

        return UserPermissions(dump=dump)

    def _gen_dump(self):
        self._dump = []
        if not self._allowed_resourses:
            return

        current_bits = ''
        for i in range(0, max(self._allowed_resourses) + 1):
            bit = '1' if i in self._allowed_resourses else '0'
            current_bits = bit + current_bits
            if len(current_bits) == 32:
                self._dump.append(int(current_bits, 2))
                current_bits = ''

        if current_bits:
            self._dump.append(int(current_bits, 2))

    def get_dump(self):
        """
        :rtype: list(int)
        """
        if self._dump is None:
            self._gen_dump()
        return self._dump

    def _restore_from_dump(self):
        self._allowed_resourses = set()
        for i, current_int in enumerate(self._dump):
            for k in range(33):
                tmp = current_int
                if k > 0:
                    tmp = current_int >> k
                if tmp == 0:
                    break

                if tmp & 1:
                    self._allowed_resourses.add(i * 32 + k)

    def get_allowed_resourses(self):
        """
        :rtype: list(int)
        """
        if self._allowed_resourses is None:
            self._restore_from_dump()

        return self._allowed_resourses

    def is_allowed(self, resource_id):
        return resource_id in self.get_allowed_resourses()
