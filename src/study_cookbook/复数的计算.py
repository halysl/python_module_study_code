# -*- coding: utf-8 -*-

"""
复数，为实数的延伸，它使任一多项式方程都有根。
复数当中有个“虚数单位”，它是的一个平方根，即。
  任一复数都可表达为，其中及皆为实数，分别称为复数之“实部”和“虚部”。
复数的发现源于三次方程的根的表达式。
数学上，“复”字表明所讨论的数域为复数，如复矩阵、复变函数等。

z＝a+bi
"""


def cal_complex_number():
    a = complex(2, 4)
    b = 3 - 5j

    print(a)
    print(b)

    print(a.real)
    print(a.imag)
    print(a.conjugate())

    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(abs(a))

if __name__ == "__main__":
    cal_complex_number()
