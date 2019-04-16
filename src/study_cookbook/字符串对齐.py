#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
简单的字符串对齐，直接使用 ljust、rjsut 或者 center 即可。
"""

def simple_format():
    text = "Hello World"
    print(text.ljust(20))
    print(text.ljust(20, "*"))
    print(text.rjust(20))
    print(text.rjust(20, "*"))
    print(text.center(20))
    print(text.center(20, "*"))

"""
复杂格式 通过format实现
"""

def complex_format():
    text = "Hello World"
    print(format(text, '>20'))
    print(format(text, '<20'))
    print(format(text, '^20'))
    print(format(text, '=>20s'))
    print(format(text, '=<20s'))
    print(format(text, '=^20s'))

if __name__ == "__main__":
    simple_format()
    complex_format()