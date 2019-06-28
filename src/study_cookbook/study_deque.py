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
from collections import deque


def max_left():
    """特定长度的队列
    """
    length = 3
    li = deque(maxlen=length)
    li.append(1)
    assert li == deque([1], maxlen=3)
    # 由于li的长度为3， 所以1+4-3 = 2，所以需要删掉两个元素，就是最老的两个元素
    li.extend([2, 3, 4, 5])
    assert li == deque([2, 3, 4, 5], maxlen=3)


def a_deque():
    """可以从左右删除的队列
    """
    li = deque()
    li.extend([1, 2, 3, 4])
    assert li == deque([1, 2, 3, 4])
    li.appendleft(5)
    assert li == deque([5, 1, 2, 3, 4])
    r = li.pop()
    assert r == 4
    r = li.popleft()
    assert r == 5

if __name__ == "__main__":
    max_left()
    a_deque()
