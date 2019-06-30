# -*- coding: utf-8 -*-

import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    # yield 之前的代码会在上下文管理器中作为 __enter__() 方法执行
    # 所有在 yield 之后的代码会作为 __exit__() 方法执行
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


def create_a_big_list():
    with timethis('create_a_big_list'):
        data = list(range(10000000))
    return data


def test_for(data):
    with timethis('test_for'):
        temp = []
        for i in data:
            if not i % 3:
                temp.append(i)
    return temp


def test_list_range(data):
    with timethis('test_list_range'):
        temp = [x for x in data if not x % 3]
    return temp


def count_10kk():
    with timethis('counting'):
        n = 10000000
        while n > 0:
            n -= 1


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


def test_list():
    items = [1, 2, 3]
    with list_transaction(items) as working:
        working.append(4)
        working.append(5)
    print(items)
    try:
        with list_transaction(items) as working:
            working.append(6)
            working.append(7)
            raise RuntimeError('Oops')
    except RuntimeError as e:
        print(e)
    print(items)

if __name__ == "__main__":
    count_10kk()
    data = create_a_big_list()
    res1 = test_for(data)
    res2 = test_list_range(data)
    print('res == res2?', res1 == res2)
    test_list()
