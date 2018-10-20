# -*- coding:utf-8 -*-


import requests
from bs4 import BeautifulSoup as bs


class HttpConnectError(Exception):
    pass


class UnknowError(Exception):
    pass


def get_info(url):
    r = requests.get(url)
    if r.status_code == 200:
        r.encoding = 'utf-8'
        return r.text
    else:
        raise HttpConnectError


try:
    url = 'http://www.baidu.com'
    result = get_info(url)
    print(result)
except HttpConnectError as e:
    print('连接错误')
except UnknowError as e:
    print(e.message)