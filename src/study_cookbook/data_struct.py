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

def decompression_assignment():
    """解压赋值
    """
    # 可迭代对象根据位置赋值
    p = (4, 5)
    x, y = p
    assert x == 4
    assert y == 5
    
    # 嵌套对象同样可以按位置赋值
    complex_list = [ 'Ash', 18, 91.1, (2012, 12, 21) ]
    name, age, score, date = complex_list
    assert name == 'Ash'
    assert age == 18
    assert score == 91.1
    assert date == (2012, 12, 21)

    # tuple内部也可以按位置取值
    complex_list = [ 'Ash', 18, 91.1, (2012, 12, 21) ]
    name, age, score, (year, mouth, day) = complex_list
    assert year == 2012
    assert mouth == 12
    assert day == 21

    # 字符串也是可迭代对象
    a, b, c, d, e = 'hello'
    assert a == 'h'
    assert b == 'e'
    assert c == d == 'l'
    assert e == 'o'

    # 不需要的值可以用占位符（自定义）
    complex_list = [ 'Ash', 18, 91.1, (2012, 12, 21) ]
    name, _1, _2, _3 = complex_list
    assert name == 'Ash'
    assert _1 == 18
    assert _2 == 91.1
    assert _3 == (2012, 12, 21)

if __name__ == "__main__":
    decompression_assignment()
