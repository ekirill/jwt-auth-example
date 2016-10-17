# -*- coding: utf-8 -*-
import json
from flask import make_response


def OK_RESULT(data=None):

    result = {
        'status': 'OK',
    }
    if data:
        result['data'] = data

    response = make_response(json.dumps(result))
    response.headers['Content-type'] = 'application/json'
    return response


def FAIL_RESULT(errors):
    result = {
        'status': 'FAIL',
        'errors': errors
    }

    response = make_response(json.dumps(result))
    response.headers['Content-type'] = 'application/json'
    return response
