#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def send_request(url):
    r = requests.get(url)
    return r.status_code


def visit_tack():
    return send_request('http://www.baidu.com')
