# -*- coding: utf-8 -*-
# 写了很多仅仅用作数据结构的类，不想写太多烦人的 __init__() 函数

import math


class Structure1:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


# Example class definitions
class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


class Point(Structure1):
    _fields = ['x', 'y']


class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    s = Stock('ACME', 50, 91.1)
    p = Point(2, 3)
    c = Circle(4.5)
    s2 = Stock('ACME', 50)
