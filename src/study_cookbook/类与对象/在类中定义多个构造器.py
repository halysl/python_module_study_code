# -*- coding: utf-8 -*-
# 使用 类方法

import time


class Date:
    """方法一：使用类方法"""
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


def example_more_init():
    a = Date(2012, 12, 21)  # Primary
    b = Date.today()  # Alternate
    print(a)
    print(b)

if __name__ == "__main__":
    example_more_init()
