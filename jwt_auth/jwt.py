# -*- coding: utf-8 -*-
"""
Simple JWT https://en.wikipedia.org/wiki/JSON_Web_Token implementation
with the only sign algorithm (HMAC-SHA256)
"""
import hashlib
import json
import base64
import binascii

from .exceptions import JWTInvalidToken, JWTVerificationError


def _base64_encode(data):
    """
    :type data: bytes
    :rtype: bytes
    """
    return base64.urlsafe_b64encode(data).replace(b'=', b'')


def _base64_decode(data):
    """
    :type data: bytes
    :rtype: bytes
    """
    rem = len(data) % 4

    if rem > 0:
        data += b'=' * (4 - rem)

    return base64.urlsafe_b64decode(data)


def _encode_dict(data):
    """
    :type data: dict
    :rtype: bytes
    """
    return _base64_encode(
        json.dumps(data, ensure_ascii=False, sort_keys=True).encode('utf-8')
    )


class JWTApi(object):
    header_bytes = _encode_dict({
        "alg": "HS256",
        "typ": "JWT"
    })

    def __init__(self, secret):
        self._secret = _base64_encode(secret.encode('utf-8'))

    def _gen_signature(self, unsigned_data):
        sig_str = self._secret + unsigned_data
        sig = str(hashlib.sha256(sig_str).hexdigest()).encode('utf-8')
        encoded = _base64_encode(sig)
        return encoded

    def dumps(self, payload):
        """
        Encodes payload in token as bytestring, storable as cookie
        :type payload: dict
        :rtype: bytes
        """
        if not payload:
            payload = {}

        payload_bytes = _encode_dict(payload)
        unsigned_data = self.header_bytes + b'.' + payload_bytes

        return unsigned_data + b'.' + self._gen_signature(unsigned_data)

    def loads(self, token):
        """
        Decodes bytestring, stored by dumps method
        :type token: bytes
        :rtype: dict
        """
        self.verify(token)

        sections = token.split(b'.')
        payload_data = sections[1]

        try:
            payload_json = _base64_decode(payload_data)
        except (binascii.Error, TypeError):
            raise JWTInvalidToken('Token payload is not valid base64 encoded data')

        try:
            payload = json.loads(payload_json.decode('utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError):
            raise JWTInvalidToken('Token payload is not a valid JSON')

        return payload

    def verify(self, token):
        """
        Verifies token against our secret.
        Raises nothing on success.
        Raises JWTVerificationError on fail.
        :type token: bytes
        """

        if not token:
            raise JWTInvalidToken('Got empty token')

        if not isinstance(token, bytes):
            raise JWTInvalidToken('Bytes expected as token')

        sections = token.split(b'.')
        if len(sections) != 3:
            raise JWTInvalidToken('Token must consist of 3 parts, separated by dot')

        unsigned_data = sections[0] + b'.' + sections[1]
        if self._gen_signature(unsigned_data) != sections[2]:
            raise JWTVerificationError('Signature does not match the token payload or our secret key')
