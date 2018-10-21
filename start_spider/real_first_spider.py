# -*- coding:utf-8 -*-
# author:light
# date:
# info:一个真正，可用的爬虫

# 选择目标：pass

import requests
from bs4 import BeautifulSoup as bs


def get_info(url, headers=None, flag=None):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        return r.text
    else:
        return requests.RequestException


if __name__ == "__main__":
    url = 'https://steamcn.com/forum.php'
    result = get_info(url)
    print(result)