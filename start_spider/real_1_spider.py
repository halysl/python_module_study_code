# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

# 选择目标：https://steamcn.com/forum.php

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
    # tag的 .contents 属性可以将tag的子节点以列表的方式输出
    soup = bs(context)
    tag = soup.head
    print('soup.head.contents', tag.contents)


def get_children(context):
    # 通过tag的 .children 生成器,可以对tag的子节点进行循环
    soup = bs(context)
    tag = soup.head
    for child in tag.children:
        print(child)


if __name__ == "__main__":
    url = 'https://steamcn.com/forum.php'
    result = get_info(url)
    # preffity_print(result)
    # get_some_info(result)
    # get_contents(result)
    get_children(result)
