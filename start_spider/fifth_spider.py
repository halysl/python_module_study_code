# -*- coding:utf-8 -*-
# author:light
# date:2018-10-20 15:00
# info:重定向相关

import requests

url = 'http://github.com'


def redirects():
    r = requests.get(url)
    print('r.url:', r.url)
    print('r.status_code:', r.status_code)
    print('r.history:', r.history)


def no_redirects():
    r = requests.get(url, allow_redirects=False)
    print('r.url:', r.url)
    print('r.status_code:', r.status_code)
    print('r.history:', r.history)


def redirects_head():
    r = requests.head('http://github.com', allow_redirects=True)
    print('r.url:', r.url)
    print('r.status_code:', r.status_code)
    print('r.history:', r.history)


if __name__ == "__main__":
    print('=====redirect get=====')
    redirects()
    print('=====no redirect get=====')
    no_redirects()
    print('=====redirect head=====')
    redirects()
