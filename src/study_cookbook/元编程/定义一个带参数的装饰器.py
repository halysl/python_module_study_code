# -*- coding: utf-8 -*-

import logging
from functools import wraps


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name or func.__module__
        log = logging.getLogger(logname)
        logmsg = message or func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


# Example use
@logged(logging.INFO)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example', 'this is a spam log')
def spam():
    print('Spam!')


if __name__ == "__main__":
    res = add(3, 4)
    print(res)
    spam()
    print("\n\n")
    res = logged(logging.CRITICAL, message="this is a critical msg")(spam)()
