#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName:
# Desc: 字符串搜索和替换
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""
import re


def replace_string_with_strmethod():
    text = 'yeah, but no, but yeah, but no, but yeah'
    text.replace('yeah', 'yep')

    print text


def replace_string_with_resub():
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

    print text

if __name__ == "__main__":
    replace_string_with_strmethod()
    replace_string_with_resub()
