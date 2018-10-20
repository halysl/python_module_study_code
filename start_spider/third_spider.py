# -*- coding:utf-8 -*-
# author:light
# date:
# info:None

import requests
import exception
from second_spider import get_text_info, get_json_info


def get_info(url, headers=None, flag=None):
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        r.encoding = 'utf-8'
    else:
        raise exception.HttpConnectError

    if not flag:
        return get_text_info(r)
    elif flag == 'text':
        return get_text_info(r)
    elif flag == 'json':
        return get_json_info(r)
    else:
        pass


if __name__ == "__main__":
    url = 'https://api.github.com/some/endpoint'
    headers = {'user-agent': 'my-app/0.0.1'}
    result = get_info(url, headers=headers)
    print(result)
