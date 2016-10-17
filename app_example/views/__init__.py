# -*- coding: utf-8 -*-
from flask import jsonify


def OK_RESULT(data=None):
    result = {
        'status': 'OK',
    }
    if data:
        result['data'] = data

    return jsonify(result)


def FAIL_RESULT(errors):
    result = {
        'status': 'FAIL',
        'errors': errors
    }

    return jsonify(result)
