# -*- coding: utf-8 -*-
# 标准切片无法对迭代器进行操作，因为迭代器没有长度，也没有索引
# 但是可以使用itertools.islice 曲线救国，原理就是生成一个特定长度的新的迭代器

import itertools


def count(n):
    while True:
        yield n
        n += 1

if __name__ == "__main__":
    c = count(100)
    print(type(c))
    try:
        c[10:20]
    except Exception as e:
        print(e.message)
    
    d = itertools.islice(c, 10, 20)
    print(type(d))
    for x in d:
        print(x)
