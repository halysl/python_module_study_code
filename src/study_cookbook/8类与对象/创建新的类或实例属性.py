# -*- coding: utf-8 -*-
# 通过定义一个描述器，你可以在底层捕获核心的实例操作(get, set, delete)，并且可完全自定义它们的行为。
# 这是一个强大的工具，有了它你可以实现很多高级功能，并且它也是很多高级库和框架中的重要工具之一。
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p09_create_new_kind_of_class_or_instance_attribute.html


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    p = Point(2, 3)
    print(p, p.x, p.y)
    print(Point.x.__get__(p, Point))
    print(Point.y.__get__(p, Point))
    p.x = 5
    print(p.x, Point.x.__get__(p, Point))
