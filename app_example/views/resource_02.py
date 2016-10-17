# -*- coding: utf-8 -*-
from app_example.auth import permission_required
from app_example.hardcode import RESOURCE_2
from flask.views import MethodView
from flask import request

from . import OK_RESULT


class Resource_02(MethodView):
    @permission_required(request, RESOURCE_2)
    def get(self):
        return OK_RESULT({'sugar_data': 24})
