#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName:
# Desc: 映射名称到序列元素(序列元素可以不通过index进行访问)
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""
from collections import namedtuple


def named_tuple():
    # 通过namedtuple创建一个命名元组类型
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub1 = Subscriber('Ash@example.com', '2010-1-1')
    # 可以像访问类属性的方式访问对应位置的值
    assert sub1.addr == sub1[0]
    assert sub1.joined == sub1[1]
    # 可以保留元组的基础操作（解压等）
    addr, joined = sub1
    assert addr == sub1[0]
    assert joined == sub1[1]

if __name__ == "__main__":
    named_tuple()
