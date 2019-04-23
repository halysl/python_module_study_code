# -*- coding: utf-8 -*-

from fractions import Fraction


def cal_fraction():
    a = Fraction(5, 4)
    b = Fraction(7, 16)

    print("a={}\tb={}\n".format(a, b))

    print("a+b={}\na-b={}\na*b={}\na/b={}\n".format(a+b, a-b, a*b, a/b))

    c = a * b
    print("c=a*b={}\nc.numerator={}\nc.denominator={}\nfloat(c)={}\n".format(
        c, c.numerator, c.denominator, float(c)))

if __name__ == "__main__":
    cal_fraction()
