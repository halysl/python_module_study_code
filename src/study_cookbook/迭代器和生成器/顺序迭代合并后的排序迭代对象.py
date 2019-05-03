# -*- coding: utf-8 -*-
# 若干个排序后的序列，合并生成一个有顺序的可迭代对象

import heapq


def example_heapq_merge():
    a = [1, 4, 7, 10]
    b = [2, 5, 6, 11]
    for c in heapq.merge(a, b):
        print(c)

if __name__ == "__main__":
    example_heapq_merge()
