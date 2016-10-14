# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import jsonify


class Ping(MethodView):
    def get(self):
        return jsonify({
            "status": "ALIVE"
        })
