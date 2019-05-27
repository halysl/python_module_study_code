# -*- coding: utf-8 -*-
import time
from functools import wraps


def timethis_with_wrap(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


def timethis_without_wrap(func):
    '''
    Decorator that reports the execution time.
    '''
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


def countdown(n: int):
    """减数
    """
    while n > 0:
        n -= 1


if __name__ == "__main__":
    countdown_wrap = timethis_with_wrap(countdown)
    countdown_nowrap = timethis_without_wrap(countdown)
    print(countdown_wrap.__name__,
          countdown_wrap.__doc__,
          countdown_wrap.__annotations__)
    print(countdown_nowrap.__name__,
          countdown_nowrap.__doc__,
          countdown_nowrap.__annotations__)
