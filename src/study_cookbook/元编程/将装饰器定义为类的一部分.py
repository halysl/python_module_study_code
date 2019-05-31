# -*- coding: utf-8 -*-

from functools import wraps


class A(object):
    def decorator1(self, func):
        @wraps(func)
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
