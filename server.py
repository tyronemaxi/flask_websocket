#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tianzhichao
File: server.py
Time: 2023/11/1 8:21 AM
"""
from flask import Flask
from app.extention.websocket import init_websocket


def create_app():
    app = Flask(__name__)
    return app


if __name__ == '__main__':
    app = create_app()
    server = init_websocket(app)
    server.run(app, host="0.0.0.0", port=8000, use_reloader=True, debug=True, logger=True, engineio_logger=True)
