# -*- coding: utf-8 -*-
from flask.views import MethodView
from . import OK_RESULT


class Ping(MethodView):
    def get(self):
        return OK_RESULT()
