# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from first_requests import get_response


def first_parse(response):
    results = list()
    soup = BeautifulSoup(response)
    for i in soup.find_all('a'):
        res = dict()
        res['tag'] = 'a'
        # res['class'] = i['class']
        # res['href'] = i['href']
        # res['name'] = i['name']
        results.append(res)
    return results


response = get_response('www.baidu.com')
result = first_parse(response)
print(result)
