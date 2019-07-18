# -*- coding: utf-8 -*-
from inspect import Signature, Parameter, signature

# 对每一个参数指定位置和默认值，生成一个签名对象
params = [Parameter("x", Parameter.POSITIONAL_OR_KEYWORD),
          Parameter("y", Parameter.POSITIONAL_OR_KEYWORD, default=42),
          Parameter("z", Parameter.KEYWORD_ONLY, default=None)]
print(params)
sig = Signature(params)
print(sig, type(sig))


def func(*args, **kwargs):
    print('\n')
    # 签名对象可以绑定真实参数，并且一一对应生成一个 bond 结构，该结构的 arguments 对象是一个字典
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)


def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')

if __name__ == "__main__":
    func(1, 2, z=3)
    func(1)
    func(1, 3)
    print(signature(Stock))
    print(signature(Point))
    s1 = Stock('ACME', 100, 490.1)
    print(s1.__dict__)
