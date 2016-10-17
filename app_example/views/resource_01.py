# -*- coding: utf-8 -*-
from flask.views import MethodView
from . import OK_RESULT, FAIL_RESULT


class Resource_01(MethodView):
    def get(self):
        return OK_RESULT({'juicy_data': 42})
