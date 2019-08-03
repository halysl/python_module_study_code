# -*- coding: utf-8 -*-

import threading
import random


def func(a):
    return a


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        print("Starting " + threading.currentThread().name)
        self.result = self.func(*self.args)
        print("Exiting " + threading.currentThread().name)

    def get_result(self):
        threading.Thread.join(self)  # 等待线程执行完毕
        try:
            return self.result
        except Exception:
            return None

if __name__ == "__main__":
    rets = []
    li = []
    for i in range(4):
        li.append(MyThread(func, (random.randint(1, 100),)))

    for l in li:
        l.start()

    for l in li:
        l.join()

    for l in li:
        rets.append(l.get_result())
    print(rets)
