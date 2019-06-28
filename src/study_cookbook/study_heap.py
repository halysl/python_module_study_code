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

import heapq
import random


def a_heap():
    """使用一个堆数据结构
    heapq是一个堆类，它拥有很多和堆结构相关的方法
    最常用的是
    nlargest(n , iterable, key)
    nsmallest(n , iterable, key)
    从一个可迭代对象中通过key取出n个元素
    """
    # 产生一个100个元素的列表，列表元素的值范围在1000内
    li = [random.randrange(1000) for _ in range(100)]
    assert heapq.nlargest(1, li)[0] == max(li)
    assert heapq.nsmallest(1, li)[0] == min(li)

    # heapy的排序底层是调用了heapify方法，使一个序列变为堆排序的结果
    # 此时可以通过heappop方法取出最小值
    heapq.heapify(li)
    assert min(li) == heapq.heappop(li)
    assert min(li) == heapq.heappop(li)


class PriorityQueue(object):
    """有优先级的队列"""
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 关键， 插入数据，数据类型为tuple，包括级别，插入时的index， 实际数据
        # 好处是heap的结构会根据三元组的前两个参数进行排序，也就是说，级别越高，在堆中被pop出的越早
        # index为了确保同级别下顺序的一致性（无法同时push两个数据）
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heap的结构特性，从列表中输出最小的值（构成的元组）
        return heapq.heappop(self._queue)[-1]


class Item():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '{!r}'.format(self.name)


def priority_queue():
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print q.pop()
    print q.pop()
    print q.pop()
    print q.pop()

if __name__ == '__main__':
    a_heap()
    priority_queue()
