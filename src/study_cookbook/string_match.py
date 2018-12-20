#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: 
# Desc: 使用正则匹配字符串
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

"""
>>> # Exact match
>>> text == 'yeah'
False
>>> # Match at start or end
>>> text.startswith('yeah')
True
>>> text.endswith('no')
False
>>> # Search for the location of the first occurrence
>>> text.find('no')
10
>>>
"""

def match_by_re():
    # re功能非常强大哦，对于只使用一次匹配，可以使用re.match(match_param, str)
    text1 = '11/27/2012'
    text2 = 'Nov 27, 2012'
    if re.match(r'\d+/\d+/\d+', text1):
        print 'Yes'
    else:
        print 'No'
    if re.match(r'\d+/\d+/\d+', text2):
        print 'yes'
    else:
        print 'no'

    # 如果需要多次匹配，但是使用同样的匹配模式，那么应该先re.compile编译为模式对象
    # 再通过模式对象的match findall等方法等方法取匹配
    datepat = re.compile(r'\d+/\d+/\d+')
    if datepat.match(text1):
        print 'Yes'
    else:
        print 'No'
    if datepat.match(text2):
        print 'yes'
    else:
        print 'no'

    # match会从头开始匹配，一旦对不上直接结束，而findall会一直查询
    text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print datepat.findall(text3)

    # 正则匹配重要的作用之一就是提取出想要的数据，这时候分组就有意义了， 用括号捕获分组
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = datepat.match(text1)
    print m.group(0)
    print m.group(1)
    print m.group(2)
    print m.group(3)
    print m.groups()


if __name__ == "__main__":
    match_by_re()