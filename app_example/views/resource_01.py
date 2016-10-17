# -*- coding: utf-8 -*-
from app_example.auth import permission_required
from app_example.hardcode import RESOURCE_1
from flask.views import MethodView
from flask import request

from . import OK_RESULT


class Resource_01(MethodView):
    @permission_required(request, RESOURCE_1)
    def get(self):
        return OK_RESULT({'juicy_data': 42})
