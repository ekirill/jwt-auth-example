#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
))


from app_example.application import create_app
create_app().run(port=8000)
