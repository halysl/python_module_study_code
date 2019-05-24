# -*- coding: utf-8 -*-
# 通过 getattr 实现

import math
import operator


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


def example_getatta_func():
    p = Point(2, 3)
    d1 = p.distance(0, 0)
    d2 = getattr(p, "distance")(0, 0)
    d3 = operator.methodcaller("distance", 0, 0)(p)
    temp = operator.methodcaller("distance", 0, 0)
    d4 = temp(p)
    print(d1, d2, d3, d4)
    print(dir(temp), type(temp))
    points = [
        Point(1, 2),
        Point(3, 0),
        Point(10, -3),
        Point(-5, -7),
        Point(-1, 8),
        Point(3, 2)
    ]
    # Sort by distance from origin (0, 0)
    points.sort(key=operator.methodcaller('distance', 0, 0))
    print(points)


if __name__ == "__main__":
    example_getatta_func()
