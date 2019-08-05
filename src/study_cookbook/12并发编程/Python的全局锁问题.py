# -*- coding: utf-8 -*-
# GIL 是 cpython 的 全局解释锁，他的原因可以看https://zhuanlan.zhihu.com/p/20953544
# 有两种解决方案，一是利用多进程，一是利用c扩展
from multiprocessing import pool


def some_work(args):
    return result


def some_thread():
    while True:
        r = pool.apply(some_work, (args))
