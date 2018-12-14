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
    """解压可迭代对象赋值给多个变量（等数量变量）
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


def decompression_assignment_to_few_param():
    """解压可迭代对象赋值给多个变量(不等数量变量)
    """
    # only in python3
    scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    # *号可以指代多个元素，最终形成一个list，也就是说middle必定是list
    first, *middle, last = scores
    assert first == 1
    assert last == 17
    assert middle ==  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    # 对于list每一项都可以做解压
    records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
    ]
    for tag, *args in records:
        if tag == 'foo':
            assert args == [1, 2]
        elif tag == 'bar':
            assert args == ['hello']

    # 字符串分割
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')
    assert uname == 'nobody'
    assert homedir == '/var/empty'
    assert sh == '/usr/bin/false'


if __name__ == "__main__":
    decompression_assignment()
    decompression_assignment_to_few_param()
