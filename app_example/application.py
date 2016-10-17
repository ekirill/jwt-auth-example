# -*- coding: utf-8 -*-
from flask import Flask
from .views.ping import Ping
from .views.resource_01 import Resource_01
from .views.resource_02 import Resource_02


def create_app():
    app = Flask(__name__)

    app.add_url_rule('/', view_func=Ping.as_view('index'))
    app.add_url_rule('/api/v1/resource_01.json', view_func=Resource_01.as_view('resource_01'))
    app.add_url_rule('/api/v1/resource_02.json', view_func=Resource_02.as_view('resource_02'))

    return app
