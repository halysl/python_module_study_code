# -*- coding:utf-8 -*-

import requests


def get_response(url):
    if not url.startswith('http'):
        url = ''.join(['http://', url])
    try:
        r = requests.get(url)
        if r.encoding != 'utf-8':
            r.encoding = 'utf-8'
        if r.status_code == 200:
            return r.text
        else:
            return r.status_code
    except requests.exceptions.ConnectionError as e:
        return '无法解析url' + '\n' + str(e.message)


if __name__ == "__main__":
    result = get_response('www.bidu.com')
    print(result)
