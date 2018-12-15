#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: 
# Desc: 对切片进行命名
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""


def named_slice():
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print li
    # 直接使用切片
    print li[3:5]
    # 对切片进行命名
    shared = slice(3, 5)
    print li[shared]
    # 可以执行切片的其他功能
    li[shared] = [13, 14]
    print li
    del li[shared]
    print li

    # 那么slice对象还有哪些属性
    print shared.start
    print shared.stop
    print shared.step


if __name__ == "__main__":
    named_slice()
