# -*- coding: utf-8 -*-
# 使用关键字参数来给被包装函数增加额外参数
# python3 特性

from functools import wraps

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)

if __name__ == "__main__":
    spam(1, 2, 3, debug=True)
