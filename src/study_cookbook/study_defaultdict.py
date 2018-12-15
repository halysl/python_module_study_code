#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: 
# Desc: 
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""
from collections import defaultdict

def default_dict():
    # defaultdict这个模块要求输入一种类型，并且自动的为dict里面的value设置类型
    dic = defaultdict(list)
    assert isinstance(dic, defaultdict)
    assert isinstance(dic['a'], list)
    dic['a'].append(1)
    assert dic['a'] == [1]

if __name__ == "__main__":
    default_dict()