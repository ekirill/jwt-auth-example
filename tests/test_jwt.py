# -*- coding: utf-8 -*-
import pytest

from jwt_auth.jwt import JWTApi
from jwt_auth.exceptions import JWTVerificationError


def test_payload_encode_decode(secret, jwt_payload_gen):
    jwt_api = JWTApi(secret)

    payload = jwt_payload_gen()
    token = jwt_api.dumps(payload)

    assert isinstance(token, bytes)

    def _base64_valid_byte(ch):
        return 'a' <= chr(ch) <= 'z' or 'A' <= chr(ch) <= 'Z' or '0' <= chr(ch) <= '9' or chr(ch) == '.'

    assert all(map(_base64_valid_byte, token))

    restored_payload = jwt_api.loads(token)
    assert payload == restored_payload


def test_secret_check(secret, another_secret, jwt_payload_gen):
    payload = jwt_payload_gen()

    jwt_api_1 = JWTApi(secret)
    jwt_api_2 = JWTApi(another_secret)

    token_2 = jwt_api_2.dumps(payload)

    with pytest.raises(JWTVerificationError):
        jwt_api_1.loads(token_2)


def test_payload_fake(secret, jwt_payload_gen):
    payload_1 = jwt_payload_gen(permissions=['read_only'])
    payload_2 = jwt_payload_gen(permissions=['*'])

    jwt_api = JWTApi(secret)

    token_1 = jwt_api.dumps(payload_1)
    token_2 = jwt_api.dumps(payload_2)

    sections_1 = token_1.split(b'.')
    sections_2 = token_2.split(b'.')

    tmp = sections_1[1]
    sections_1[1] = sections_2[1]
    sections_2[1] = tmp

    token_1 = b'.'.join(sections_1)
    token_2 = b'.'.join(sections_2)

    with pytest.raises(JWTVerificationError):
        jwt_api.loads(token_1)

    with pytest.raises(JWTVerificationError):
        jwt_api.loads(token_2)
