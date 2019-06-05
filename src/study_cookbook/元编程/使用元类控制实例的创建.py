# -*- coding: utf-8 -*-
# 通过改变实例创建方式来实现单例、缓存或其他类似的特性
# 改变 __call__ 方法
import weakref


class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print("print x={}".format(x))


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class SingletonSpam(metaclass=Singleton):
    def __init__(self):
        print("create self: {}".format(self))


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


class CacheSpam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name

if __name__ == "__main__":
    Spam.grok(100)
    try:
        s = Spam()
    except TypeError as e:
        print(e)

    a = SingletonSpam()
    b = SingletonSpam()
    c = SingletonSpam()
    print(a is b, a is c)

    a = CacheSpam("a")
    b = CacheSpam("b")
    c = CacheSpam("a")
    print(a is b, a is c)
