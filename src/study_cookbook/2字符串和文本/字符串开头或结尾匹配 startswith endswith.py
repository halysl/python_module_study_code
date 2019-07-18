#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName:
# Desc: 字符串开头或结尾匹配 startswith endswith
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""


def match():
    a = 'data_struct.py'
    with open(a, 'r') as f:
        data = f.readlines()
        for i in data:
            if i.startswith('#!/usr/bin/env python'):
                print '--START--', i
            if i.endswith('"__main__":\n'):
                print '--MAIN--', i

if __name__ == "__main__":
    match()
