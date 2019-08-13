#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import (
    Blueprint,
)

main = Blueprint('healthz', __name__)

@main.route('/healthz', methods=['GET', 'HEAD'])
def webhook():
    return 'health', 200