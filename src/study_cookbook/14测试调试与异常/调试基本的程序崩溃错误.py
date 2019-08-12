# -*- coding: utf-8 -*-
import traceback
import sys


def func(n):
    return n + 10

# func('Hello')

# python3 -i 调试基本的程序崩溃错误.py
# 以上指令会打开 Python shell


try:
    func('hello')
except:
    print('**** AN ERROR OCCURRED ****')
    traceback.print_exc(file=sys.stderr)


def sample(n):
    if n > 0:
        sample(n-1)
    else:
        traceback.print_stack(file=sys.stderr)

sample(5)
