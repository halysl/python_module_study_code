import time
from functools import wraps


def func(judge=True):
    def re_true():
        print 'judge is True'

    def re_false():
        print 'judge is False'

    if judge:
        return re_true
    else:
        return re_false


def first_deco(func):
    @wraps(func)
    def wrap():
        print time.localtime()
        func()
        print time.localtime()
    return wrap


@first_deco
def fun_1():
    print('hello')


print(fun_1())

print(fun_1.__name__)
