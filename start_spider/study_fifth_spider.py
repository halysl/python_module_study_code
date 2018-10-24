# -*- coding:utf-8 -*-
# author:light
# date:2018-10-20 15:00
# info:重定向相关
# slogan:狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。

import requests

url = 'http://github.com'


def redirects():
    # GET、OPTIONS、POST、PUT、PATCH 或者 DELETE，默认重定向，head默认不重定向
    r = requests.get(url)
    print('origin url', url)
    print('r.url:', r.url)
    print('r.status_code:', r.status_code)
    print('r.history:', r.history)


def no_redirects():
    # 虽然默认重定向，但是可以通过allow_redirects修改
    r = requests.get(url, allow_redirects=False)
    print('origin url', url)
    print('r.url:', r.url)
    print('r.status_code:', r.status_code)
    print('r.history:', r.history)


def redirects_head():
    # 虽然默认不重定向，但是可以通过allow_redirects修改
    r = requests.head('http://github.com', allow_redirects=True)
    print('origin url', url)
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
