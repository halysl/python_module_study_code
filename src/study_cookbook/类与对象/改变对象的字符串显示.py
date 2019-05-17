# -*- coding: utf-8 -*-
# 通过重定义 __str__ and __repr__


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point value=({0.x!r}, {0.y!r})>".format(self)

    def __str__(self):
        return "({0.x!s}, {0.y!s})".format(self)


def example_point():
    p = Point(1, 2)
    print(repr(p))
    print(p)
    print('p is {0!r}'.format(p))
    print('p is {0}'.format(p))

if __name__ == "__main__":
    example_point()
