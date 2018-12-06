#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: study_different_call.py
# Desc: 前后两次的调用会产生不同的结果
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-12-06 17:29
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""
import os


def fun1():
    print('1')


def fun2():
    print('2')


def fun3():
    file_path = os.path.abspath(__file__)
    result = []
    # 读取当前所有文件保存到list
    with open(file_path, 'r') as f:
        for line in f.readlines():
            result.append(line)
    # 遍历列表，对fun1()的调度注释掉
    for index, value in enumerate(result):
        if value.startswith('    fun1()'):
            result[index] = '#    fun1()\n'
    # 把列表内容全部写入当前文件
    with open(file_path, 'w') as f:
        for line in result:
            f.write(line)


if __name__ == "__main__":
    fun1()
    fun2()
    fun3()
