#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: 
# Desc:  对字典进行运算（主要针对value）
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""

def calc_dict(dic):
    # sorted dict,只对key排序
    print sorted(dic)
    # sort dict.items(),根据key对字典元素排序
    print sorted(dic.items())
    # sort dict.items() key=lambda item:item[1] 根据value对字典元素排序
    print sorted(dic.items(), key=lambda item: item[1])

    # 利用zip对字典进行重新组装，再根据key进行排序（也就是原来的value）
    print sorted(zip(dic.values(), dic.keys()))



if __name__ == "__main__":
    prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
    }
    calc_dict(prices)
