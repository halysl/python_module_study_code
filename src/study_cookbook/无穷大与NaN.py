# -*- coding: utf-8 -*-

"""
python 没有明确的标示无限大、无限小和空值，
但可以通过float声明
"""
import math


def create_inf():
    a = float("inf")
    b = float("-inf")
    c = float("nan")
    return a, b, c


def calc(a, b, c):
    print("a={}\ttype(a)={}".format(a, type(a)))
    print("b={}\ttype(b)={}".format(b, type(b)))
    print("c={}\ttype(c)={}".format(c, type(c)))
    
    print("\nmath.isinf(a)={}\nmath.isinf(b)={}\nmath.isinf(c)={}".format(
        math.isinf(a), math.isinf(b), math.isinf(c)))
    print("\nmath.isnan(a)={}\nmath.isnan(b)={}\nmath.isnan(c)={}".format(
        math.isnan(a), math.isnan(b), math.isnan(c)))

    print("\na+45={}\na*10={}\na/10={}\n10/a={}\na/a={}".format(
        a+45, a*10, a/10, 10/a, a/a))
    
    x = float("nan")
    y = float("nan")
    print("\nx={}\ty={}\nx == y >> {}\nx is y >> {}".format(
        x, y, x == y, x is y))

if __name__ == "__main__":
    x = create_inf()
    calc(*x)
