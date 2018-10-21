# -*- coding:utf-8 -*-
# author:light
# date:
# info:None

import requests
import exception
from second_spider import get_text_info, get_json_info
from forth_spider import get_session_info


def get_session():
    return requests.session()


def get_info(url, flag=None):
    s = get_session()
    r = s.get(url)
    if r.status_code == requests.codes.ok:
        r.encoding = 'utf-8'
    else:
        raise exception.HttpConnectError

    if not flag:
        return get_text_info(r)
    elif flag == 'text':
        return get_text_info(r)
    elif flag == 'json':
        return get_json_info(r)
    elif flag == 'cookies':
        return get_session_info(r)
    else:
        pass
