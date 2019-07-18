# -*- coding: utf-8 -*-
# 使用了wrap的可以通过 __wrapped__ 来访问，但不应全部相信
# 如果有多个装饰器，那么大部分情况下只会绕过一层，因为从形来看，装饰器也是一个函数
# @staticmethod 和 @classmethod 它们把原始函数存储在属性 __func__ 中
from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, *kwargs)
    return wrapper


@logged
def add(x, y):
    return x + y


if __name__ == "__main__":
    res1 = add(3, 4)
    print(res1)
    origin_add = add.__wrapped__
    res2 = origin_add(3, 4)
    print(res2)
