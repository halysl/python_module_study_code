# -*- coding:utf-8 -*-
# author:light
# date:
# info:一个真正，可用的爬虫

# 选择目标：pass

import requests
from bs4 import BeautifulSoup as bs


def get_info(url, headers=None, flag=None):
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        r.encoding = 'utf-8'
    else:
        return requests.RequestException

    if not flag:
        return r.text


def preffity_print(context):
    soup = bs(context)
    print(soup.prettify())


if __name__ == "__main__":
    url = 'https://steamcn.com/forum.php'
    result = get_info(url)
    preffity_print(result)
