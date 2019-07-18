# -*- coding: utf-8 -*-

from decimal import Decimal
from decimal import localcontext


def unprecision():
    a = 4.2
    b = 2.1
    print("{0}\n{1}\n{2}\n".format(a, b, a+b))
    print("(a + b) == 6.3 >>> {0}".format((a + b) == 6.3))


def precision():
    # decimal 模块的一个主要特征是允许你控制计算的每一方面，包括数字位数和四舍五入运算。
    a = Decimal('4.2')
    b = Decimal('2.1')
    print("{0}\n{1}\n{2}\n".format(a, b, a+b))
    print("(a + b) == 6.3 >>> {0}".format((a + b) == Decimal('6.3')))


def control_your_number():
    a = Decimal('1.3')
    b = Decimal('1.7')
    print("a / b = {}".format(a / b))

    with localcontext() as ctx:
        ctx.prec = 3
        print("3位小数 a / b = {}".format(a / b))
    with localcontext() as ctx:
        ctx.prec = 50
        print(a / b)
        print("50位小数 a / b = {}".format(a / b))


def description():
    # decimal 模块实现了IBM的”通用小数运算规范”。不用说，有很多的配置选项这本书没有提到。
    # Python新手会倾向于使用 decimal 模块来处理浮点数的精确运算。
    # 然而，先理解你的应用程序目的是非常重要的。
    # 如果你是在做科学计算或工程领域的计算、电脑绘图，或者是科学领域的大多数运算，
    # 那么使用普通的浮点类型是比较普遍的做法。
    # 其中一个原因是，在真实世界中很少会要求精确到普通浮点数能提供的17位精度。
    # 因此，计算过程中的那么一点点的误差是被允许的。
    # 第二点就是，原生的浮点数计算要快的多-有时候你在执行大量运算的时候速度也是非常重要的。
    pass

if __name__ == "__main__":
    unprecision()
    precision()
    control_your_number()
