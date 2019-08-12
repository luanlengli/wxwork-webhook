#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import (
    Flask,
)

from routes.webhook import main as webhook
from utils.get_opt import get_args


def register_routes(app, command_args):
    # 注册路由
    app.register_blueprint(webhook)
    return app


def configured_app(command_args):
    # 初始化app
    app = Flask(__name__)
    app = register_routes(app, command_args)
    return app


if __name__ == '__main__':
    command_args = get_args()
    print("command_args = {}".format(command_args))
    config = dict(
        debug=False,
        host=command_args['address'],
        port=command_args['port'],
        threaded=True,
    )
    app = configured_app(command_args)
    app.run(**config)
