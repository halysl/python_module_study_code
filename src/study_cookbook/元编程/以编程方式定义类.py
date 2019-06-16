# -*- coding： utf-8-*-
import types


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost,
}

# new_class 的参数分别为，类名、父类元组、关键字参数、类成员变量填充类字典的回掉函数
Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__

s = Stock('ABCD', 50, 1.23)
print(s)
print(s.cost())


class Spam(Base, debug=True, typecheck=False):
    pass

Spam = types.new_class('Spam', (Base,),
                       {'debug': True, 'typecheck': False},
                       lambda ns: ns.update(cls_dict))
