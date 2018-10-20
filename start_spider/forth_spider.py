# -*- coding:utf-8 -*-
# author:light
# date:2018-10-20 14:00
# info:查看返回的cookies


import requests
import exception
from second_spider import get_text_info, get_json_info


def get_info(url, headers=None, flag=None):
    r = requests.get(url, headers=headers)
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


def get_session_info(response):
    if response.cookies:
        return response.cookies
    else:
        return None


if __name__ == "__main__":
    url = 'http://www.baidu.com'
    result = get_info(url, flag='cookie')
    print(result)
