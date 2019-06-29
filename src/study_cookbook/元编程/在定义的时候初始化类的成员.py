# -*- coding: utf-8 -*-
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p19_initializing_class_members_at_definition_time.html
# 没看懂

import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls, args)


class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']


class Point(StructTuple):
    _fields = ['x', 'y']

if __name__ == "__main__":
    s = Stock('ACME', 50, 91.1)
    print(s, s[0], s.name)
    print(s.shares * s.price)
