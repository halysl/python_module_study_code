# -*- coding: utf-8 -*-
# 类装饰器


def log_getattribute(cls):
    # 原理是，将类的__getattribute__放在一个新的__getattribute__里面，这样就可以做多余的事
    # Get the original implementation
    orig_getattribute = cls.__getattribute__

    # Make a new definition
    def new_getattribute(self, name):
        print('getting:', name)
        return orig_getattribute(self, name)

    # Attach to the class and return
    cls.__getattribute__ = new_getattribute
    return cls


@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


if __name__ == "__main__":
    a = A(42)
    print(a.x)
    print(a.spam())
