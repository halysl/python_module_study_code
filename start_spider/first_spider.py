# -*- coding:utf-8 -*-


import requests
import exception

def get_info(url):
    r = requests.get(url)
    if r.status_code == 200:
        r.encoding = 'utf-8'
        return r.text
    else:
        raise exception.HttpConnectError


if __name__ == "__main__":
    try:
        url = 'http://www.baidu.com'
        result = get_info(url)
        print(result)
    except exception.HttpConnectError as e:
        print('连接错误')
    except exception.UnknowError as e:
        print(e.message)
