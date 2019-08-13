#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import (
    Blueprint,
    request,
    abort,
)
import requests, json

from utils.get_opt import get_args
from utils.tools import json_to_markdown

main = Blueprint('webhook', __name__)


def wxwork_webhook(markdown_data, command_args):
    context_data = dict(
        msgtype="markdown",
        markdown=markdown_data,
    )
    print("context_data = {}".format(context_data))
    webhook_url = command_args['wxwork_webhook']
    response = requests.post(
        webhook_url,
        data=json.dumps(context_data),
        headers={
            'Content-Type': 'application/json'
        }
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )


@main.route('/webhook', methods=['POST'])
def webhook():
    json_data=request.json
    print("alertmanager data = {}".format(json_data))
    command_args = get_args()
    # print("webhook command_args {}".format(command_args))
    if request.method == 'POST':
        markdown_data = json_to_markdown(json_data)
        print("webhook markdown data = {}".format(markdown_data))
        wxwork_webhook(markdown_data=markdown_data, command_args=command_args)
        return '', 200
    else:
        abort(400)
