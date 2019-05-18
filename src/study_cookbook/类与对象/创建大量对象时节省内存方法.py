# -*- coding: utf-8 -*-
# 利用 __slots__ 特性
# __slots__ 有多种用途，包括限定类属性和节省内存


class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{0.year}年{0.month}月{0.day}日".format(self)


def example_slots():
    d = Date(2019, 5, 18)
    print(d)
    for x in dir(d):
        res = getattr(d, x)
        print(res)

if __name__ == "__main__":
    example_slots()
