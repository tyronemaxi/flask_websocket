#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tianzhichao
File: websocket.py
Time: 2023/11/1 8:23 AM
"""
import typing

from flask_socketio import SocketIO, emit

if typing:
    from flask import Flask


def init_websocket(app: Flask):
    """
    websocket 初始化
    :param app: flask api 资源
    :return:
    """
    socket_server = SocketIO(app, cors_allowed_origins='*', async_mode="gevent", logger=True, engineio_logger=True)

    return socket_server

