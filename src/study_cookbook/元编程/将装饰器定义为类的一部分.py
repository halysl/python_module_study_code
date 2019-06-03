# -*- coding: utf-8 -*-

from functools import wraps


class A(object):
    def decorator1(self, func):
        @wraps(func)
        # 注意 wrapper() 函数没有 self
        def wrapper(*args, **kwargs):
            print("Decorator1")
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorator2(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator2")
            return func(*args, **kwargs)
        return wrapper


class B(A):
    # 虽然继承了 A，但是还没实例化，所以不能直接 decorator2
    @A.decorator2
    def test():
        pass


if __name__ == "__main__":
    a = A()

    @a.decorator1
    def spam():
        print("hello")

    @A.decorator2
    def grok():
        print("world")

    spam()
    grok()
