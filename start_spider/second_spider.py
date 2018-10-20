# -*- coding:utf-8 -*-

# author:light
# date:
# info:None


import requests
import exception


def get_info(url, flag):
    r = requests.get(url)
    if r.status_code == 200:
        r.encoding = 'utf-8'
    else:
        raise exception.HttpConnectError

    if flag == 'text':
        return get_text_info(r)
    elif flag == 'json':
        return get_json_info(r)
    else:
        pass


def get_json_info(response):
    return response.json()


def get_text_info(response):
    return response.text


if __name__ == "__main__":
    url = 'https://api.github.com/events'
    result = get_info(url, 'json')
    print(result)
