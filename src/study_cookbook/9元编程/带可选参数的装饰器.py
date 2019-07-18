#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps, partial
import logging


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    """这里的写法怪怪的，但是 「理解装饰器的调用」
    """
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


@logged
# Example use
# add = logged(add)，所以装饰器的参数就是默认的
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name='example')
# spam = logged(level=logging.CRITICAL, name='example')(spam)
# 由于 logged 调用的时候，func为空，所以触发 partial 返回一个有参数的 logged，再接受 spam
def spam():
    print('Spam!')


if __name__ == "__main__":
    print(add(3, 4))
    spam()
