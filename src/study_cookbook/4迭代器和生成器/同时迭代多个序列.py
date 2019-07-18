# -*- coding: utf-8 -*-
# zip()的使用

from itertools import zip_longest


def example_zip():
    xl = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    yl = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("序列1长度为{}，序列2长度为{}".format(len(xl), len(yl)))
    for x, y in zip(xl, yl):
        print(x, y)
    xl = [1, 2, 3, 4, 5, 6, 7, 8]
    yl = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("序列1长度为{}，序列2长度为{}".format(len(xl), len(yl)))
    for x, y in zip(xl, yl):
        print(x, y)
    xl = [1, 2, 3, 4, 5, 6, 7, 8]
    yl = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("序列1长度为{}，序列2长度为{}".format(len(xl), len(yl)))
    for x in zip_longest(xl, yl):
        print(x)
    print("序列1长度为{}，序列2长度为{}".format(len(xl), len(yl)))
    for x in zip_longest(xl, yl, fillvalue=0):
        print(x)

if __name__ == "__main__":
    example_zip()
