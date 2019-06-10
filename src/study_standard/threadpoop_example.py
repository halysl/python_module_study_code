# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor


class test():
    executor = ThreadPoolExecutor(30)

    def hello(self):
        for i in range(10):
            self.executor.submit(self.say_hello, i)

    def say_hello(self, i):
        print("hello world {}".format(i))


if __name__ == "__main__":
    test().hello()
