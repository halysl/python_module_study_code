# -*- coding: utf-8 -*-
class NoMixedCaseMeta(type):
    # 对类的所有方法名进行大小写检测
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)


class Root(metaclass=NoMixedCaseMeta):
    pass


class A(Root):
    def foo_bar(self):  # Ok
        pass


class B(Root):
    def fooBar(self):  # TypeError
        pass
