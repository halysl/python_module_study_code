# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

import requests
import exception


def get_info(url, flag=None):
    r = requests.get(url)
    if r.status_code == 200:
        r.encoding = 'utf-8'
    else:
        raise exception.HttpConnectError

    if not flag:
        return get_text_info(r)
    elif flag == 'text':
        return get_text_info(r)
    elif flag == 'json':
        return get_json_info(r)
    else:
        pass


def get_json_info(response):
    return response.json()


def get_text_info(response):
    return response.text


if __name__ == "__main__":
    url = 'https://api.github.com/events'
    result = get_info(url, 'json')
    print(result)
