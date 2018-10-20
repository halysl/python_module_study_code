# -*- coding:utf-8 -*-
# author:light
# date:2018-10-20 10:00
# info:基础爬虫

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
