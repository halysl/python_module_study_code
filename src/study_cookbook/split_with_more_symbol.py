#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: 
# Desc: 使用多个界定符分割字符串,使用str.split()会返回一个列表无法再次split，只有循环列表split，产生的数据结构不优雅
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 天不生我李淳罡，剑道万古如长夜。
#=============================================================================
"""
import re

def re_split(line):
    # 通过re.split 直接将分号、冒号和空格以及多余的空格切割掉
    res = re.split(r'[;,\s]\s*', line)
    return res


if __name__ == "__main__":
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    print 'origin line:\n\t{0}'.format(line)
    res = re_split(line)
    print res