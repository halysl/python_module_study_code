# -*- coding:utf-8 -*-
# author:light
# date:2018-10-20 12:00
# info:添加headers

import requests
import exception
from second_spider import get_text_info, get_json_info


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
    else:
        pass


if __name__ == "__main__":
    url = 'https://api.github.com/some/endpoint'
    # 注意: 定制 header 的优先级低于某些特定的信息源，例如：
    # 如果在 .netrc 中设置了用户认证信息，使用 headers= 设置的授权就不会生效。而如果设置了 auth= 参数，``.netrc`` 的设置就无效了。
    # 如果被重定向到别的主机，授权 header 就会被删除。
    # 代理授权 header 会被 URL 中提供的代理身份覆盖掉。
    # 在我们能判断内容长度的情况下，header 的 Content-Length 会被改写。
    headers = {'user-agent': 'my-app/0.0.1'}
    result = get_info(url, headers=headers)
    print(result)
