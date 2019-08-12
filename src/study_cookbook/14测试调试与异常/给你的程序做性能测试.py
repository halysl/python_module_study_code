# -*- coding: utf-8 -*-
# 有多种方法可以检测程序性能，主要从不同的层级结构来看待

# 一、Unix 或者 Linux 直接 “time python xxx.py” 即可拿到程序执行时间
# bash % time python3 xxx.py
# real 0m13.937s
# user 0m12.162s
# sys  0m0.098s

# 二、需要一个程序各个细节的详细报告，使用 cProfile 模块
# python3 -m cProfile xxx.py
# 859647 function calls in 16.016 CPU seconds

# Ordered by: standard name

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 263169    0.080    0.000    0.080    0.000 someprogram.py:16(frange)
#     513    0.001    0.000    0.002    0.000 someprogram.py:30(generate_mdel)
# 262656    0.194    0.000   15.295    0.000 someprogram.py:32(<genexpr>)
#     1    0.036    0.036   16.077   16.077 someprogram.py:4(<module>)
# 262144   15.021    0.000   15.021    0.000 someprogram.py:4(in_mandelbrot)
#     1    0.000    0.000    0.000    0.000 os.py:746(urandom)
#     1    0.000    0.000    0.000    0.000 png.py:1056(_readable)
#     1    0.000    0.000    0.000    0.000 png.py:1073(Reader)
#     1    0.227    0.227    0.438    0.438 png.py:163(<module>)
#     512    0.010    0.000    0.010    0.000 png.py:200(group)

# 三、需要对函数进行性能测试

import time
from functools import wraps
from contextlib import contextmanager
from timeit import timeit


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1

# 四、需要对代码块进行性能测试


@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} : {}'.format(label, end - start))


def test_cost_time():
    with timeblock('counting'):
        n = 10000000
        while n > 0:
            n -= 1

# 五、需要对表达式或者小段代码进行性能测试，使用 timeit 模块


def test_timeit():
    res = timeit('math.sqrt(2)', 'import math', number=10000000)
    res2 = timeit('sqrt(2)', 'from math import sqrt', number=10000000)
    print(res, res2)
