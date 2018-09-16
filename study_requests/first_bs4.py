# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from first_requests import get_response


def first_parse(response):
    res = dict()
    soup = BeautifulSoup(response)
    title = soup.title.string

    res['title'] = title
    return soup.prettify()


response = get_response('www.baidu.com')
result = first_parse(response)
print(result)
