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


def get_some_info(context):
    soup = bs(context)
    print('soup.head:', soup.head)
    print('soup.title:', soup.title)

    print('soup.head.name:', soup.head.name)
    print('soup.title.name', soup.title.name)

    print('soup.find_all(a):', soup.find_all('a'))


def get_contents(context):
    soup = bs(context)
    print('soup.head.contents', soup.head.contents)


def get_children(context):
    soup = bs(context)
    for child in soup.head.children:
        print(child)


if __name__ == "__main__":
    url = 'https://steamcn.com/forum.php'
    result = get_info(url)
    # preffity_print(result)
    # get_some_info(result)
    # get_contents(result)
    get_children(result)
