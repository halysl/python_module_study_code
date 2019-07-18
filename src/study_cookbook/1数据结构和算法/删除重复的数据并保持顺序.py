#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName:
# Desc:  从序列中，删除重复的数据并保持顺序
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""


def dedupe(items):
    """仅针对可hash的元素，通过set确定唯一性
    """
    seen = set()
    for item in items:
        # 如果元素还不在这个set中，就手动的去添加它
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_with_unhashable(items, key=None):
    """针对不可hash的元素，只有通过特定的key进行判定是否唯一
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def delete_repeat_with_order(li, hashable=True):
    print li
    if hashable:
        # set可以去除重复元素，但无法保证顺序
        print set(li)
        # 保持顺序的删除重复元素
        print list(dedupe(li))
    else:
        # 通过判断 每一个元素的x值和y值确定唯一性
        res = dedupe_with_unhashable(li,  key=lambda d: (d['x'], d['y']))
        print list(res)

if __name__ == "__main__":
    li = [1, 5, 2, 1, 9, 1, 5, 10]
    delete_repeat_with_order(li)

    a = [
        {'x': 1, 'y': 2},
        {'x': 1, 'y': 3},
        {'x': 1, 'y': 2},
        {'x': 2, 'y': 4}
    ]
    delete_repeat_with_order(a, hashable=False)
