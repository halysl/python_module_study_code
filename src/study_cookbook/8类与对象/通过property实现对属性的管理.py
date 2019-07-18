# -*- coding: utf-8 -*-
import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


class Person(object):
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

if __name__ == "__main__":
    p = Person("light")
    print(p)
    print(p.first_name)
    print(dir(Person.first_name))

    c = Circle(2.0)
    print(dir(c))
    print("面积\t\t\t直径\t\t周长\t\t\t半径")
    print("{}\t{}\t\t{}\t{}".format(c.area, c.diameter, c.perimeter, c.radius))
