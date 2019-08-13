#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import (
    Flask,
)

from routes.webhook import main as webhook
from routes.healthz import main as healthz
from utils.get_opt import get_args


def register_routes(app):
    # 注册路由
    app.register_blueprint(webhook)
    app.register_blueprint(healthz)
    return app


def configured_app():
    # 初始化app
    app = Flask(__name__)
    app = register_routes(app)
    return app

def run():
    command_args = get_args()
    print("command_args = {}".format(command_args))
    config = dict(
        debug=False,
        host=command_args['listen'],
        port=command_args['port'],
        threaded=True,
    )
    app = configured_app()
    app.run(**config)

if __name__ == '__main__':
    run()