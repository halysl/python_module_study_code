#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: 
# Desc: 从字典中提取子集,一个很多field的字典提取出特定条件的kv形成新的字典
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""

def get_childset_with_dict_derivation(date):
    # 通过字典推导得到对应的字典子集
    value_bigger_200 = {k:v for k, v in date.items() if v > 200}
    names = date.keys()[1:-1]
    item_in_1_to_last = {k:v for k, v in date.items() if k in names}

    print value_bigger_200
    print item_in_1_to_last


if __name__ == "__main__":
    prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
    }
    get_childset_with_dict_derivation(prices)

