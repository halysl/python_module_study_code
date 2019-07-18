#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName:
# Desc: 过滤序列元素(列表推导或filter)
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""


def fliter_by_list_derivation(data):
    # 通过列表推导式找到大于零的元素
    res = [i for i in data if i > 0]
    return res


def fliter_by_fliter(data):
    # 通过一个filter函数（根据条件返回True/False）进行判断
    def is_bigger_0(val):
        if val > 0:
            return True
        else:
            return False

    res = list(filter(is_bigger_0, data))
    return res


if __name__ == "__main__":
    li = [1, 4, -5, 10, -7, 2, 3, -1]
    res1 = fliter_by_fliter(li)
    res2 = fliter_by_list_derivation(li)
    assert res1 == res2
