# -*- coding: utf-8 -*-
# 通过 __new__ 实现
from time import localtime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


def example_new_object():
    d1 = Date.__new__(Date)
    print(d1, d1.__dict__)
    d2 = Date.__new__(Date)
    setattr(d2, "year", "1")
    setattr(d2, "month", "2")
    setattr(d2, "day", "3")
    print(d2, d2.__dict__)
    d3 = Date.today()
    print(d3, d3.__dict__)


if __name__ == "__main__":
    example_new_object()
