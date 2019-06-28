#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName:
# Desc: 字典按插入顺序排序
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""

import json
from collections import OrderedDict


def base_dict():
    d = dict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    res = json.dumps(d)
    print(res)


def order_dict():
    # orderdict记录字典的插入顺序
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    res = json.dumps(d)
    print(res)
    # 再次赋值不影响插入顺序
    d['foo'] = 5
    res = json.dumps(d)
    print(res)
    # 但可以通过删除kv的方式重新插入
    del d['foo']
    d['foo'] = 6
    res = json.dumps(d)
    print(res)

if __name__ == "__main__":
    base_dict()
    print('=============')
    order_dict()
