# -*- coding: utf-8 -*-
from flask.views import MethodView
from . import OK_RESULT, FAIL_RESULT


class Resource_02(MethodView):
    def get(self):
        return OK_RESULT({'sugar_data': 24})
