# -*- coding: utf-8 -*-
from flask import Flask
from .views import Ping


def create_app():
    app = Flask(__name__)

    app.add_url_rule('/', view_func=Ping.as_view('index'))

    return app
