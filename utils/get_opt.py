#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser(description='A Simple Alertmanager Webhook For Wechat Enterprise!')

    parser.add_argument(
        '-w',
        '--wxwork-webhook',
        action='store',
        metavar='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxx',
        type=str,
        nargs='?',
        const='None',
        required=True,
        help='wxwork webhook url',
    )

    parser.add_argument(
        '-l',
        '--listen',
        action='store',
        metavar='0.0.0.0',
        type=str,
        nargs='?',
        default='0.0.0.0',
        required=False,
        help='listen address'
    )

    parser.add_argument(
        '-p',
        '--port',
        action='store',
        metavar='5233',
        type=str,
        nargs='?',
        default='5233',
        required=False,
        help='listen port'
    )

    # parser.add_argument(
    #     '--at-all',
    #     action='store',
    #     metavar='false',
    #     type=str,
    #     nargs='?',
    #     default='false',
    #     required=False,
    #     help='@all in wxwork'
    # )
    #
    # parser.add_argument(
    #     '--at',
    #     action='store',
    #     metavar='false',
    #     type=str,
    #     nargs='*',
    #     help='@someone in wxwork, --at a b c d'
    # )

    return parser.parse_args().__dict__