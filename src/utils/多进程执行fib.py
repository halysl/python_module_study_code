# -*- coding: utf-8 -*-

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from get_run_time import exec_time


def fib(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    while n - 2:
        a, b = b, a + b
        n -= 1
    return b


def get_more_fib_process():
    leng = [100, 1000, 100, 1000]
    with exec_time():
        with ProcessPoolExecutor(4) as pool:
            futures = [pool.submit(fib, arg) for arg in leng]
            return [f.result() for f in futures]


def get_more_fib_thread():
    leng = [100, 1000, 100, 1000]
    with exec_time():
        with ThreadPoolExecutor(4) as pool:
            futures = [pool.submit(fib, arg) for arg in leng]
            return [f.result() for f in futures]

if __name__ == "__main__":
    data = get_more_fib_process()
    print(data)
    data = get_more_fib_thread()
    print(data)
