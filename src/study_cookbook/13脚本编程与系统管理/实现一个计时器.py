# -*- coding: utf-8 -*-
# 记录程序执行多个任务所花费的时间


import time


class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()


def test():
    def countdown(n):
        while n > 0:
            n -= 1

    t = Timer()
    t.start()
    countdown(100000)
    t.stop()
    print(t.elapsed)

    with Timer() as t2:
        countdown(100000)
    print(t2.elapsed)

if __name__ == "__main__":
    test()
