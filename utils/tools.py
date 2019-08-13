#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import (
    render_template
)


def json_to_markdown(json_data):
    alerts_num = len(json_data["alerts"])
    alert_name = json_data["groupLabels"]["alertname"]
    externalURL = json_data["externalURL"]
    alert_reciever = json_data["receiver"]
    externalURL = "{}#/alerts?receiver={}".format(externalURL, alert_reciever)
    alert_messages = []
    for i in range(alerts_num):
        message = dict(
            labels=json_data["alerts"][i]["labels"],
            annotations=json_data["alerts"][i]["annotations"],
            generatorURL=json_data["alerts"][i]["generatorURL"],
            startsAt=json_data["alerts"][i]["startsAt"],
            endsAt=json_data["alerts"][i]["startsAt"],
        )
        alert_messages.append(message)
    return render_template(
        'markdown.j2',
        alert_name=alert_name,
        external_url=externalURL,
        alert_messages=alert_messages,
    )
