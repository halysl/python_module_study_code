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
from study_4_spider import get_session_info


def get_session():
    s = requests.Session()
    # 会话也可用来为请求方法提供缺省数据。
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})
    return s


def get_info(url, flag=None):
    s = get_session()
    r = s.get(url)
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


if __name__ == "__main__":
    url = 'http://httpbin.org/cookies/set/sessioncookie/123456789'
    result = get_info(url)
    print(result)
