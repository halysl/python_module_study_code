# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

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
