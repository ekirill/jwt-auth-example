# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def ping():
    return "OK, I'm alive"
