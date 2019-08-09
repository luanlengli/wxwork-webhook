#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='A Simple Alertmanager Webhook For Wechat Enterprise!')

    parser.add_argument(
        '--weixin-webhook',
        action='store',
        metavar='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxx',
        type=str,
        nargs='?',
        const='None',
        required=True,
        help='weixin webhook url',
    )

    parser.add_argument(
        '--address',
        action='store',
        metavar='0.0.0.0',
        type=str,
        nargs='?',
        default='0.0.0.0',
        help='bind address'
    )

    parser.add_argument(
        '--port',
        action='store',
        metavar='5233',
        type=str,
        nargs='?',
        default='5233',
        help='listen port'
    )

    return parser.parse_args().__dict__