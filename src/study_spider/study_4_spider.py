# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

import requests
import exception
from study_2_spider import get_text_info, get_json_info


def get_info(url, headers=None, flag=None):
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        r.encoding = 'utf-8'
    else:
        raise exception.HttpConnectError

    if not flag:
        return get_text_info(r)
    elif flag == 'text':
        return get_text_info(r)
    elif flag == 'json':
        return get_json_info(r)
    elif flag == 'cookies':
        return get_session_info(r)
    else:
        pass


def get_session_info(response):
    if response.cookies:
        return response.cookies
    else:
        return None


if __name__ == "__main__":
    url = 'http://www.baidu.com'
    result = get_info(url, flag='cookie')
    print(result)
