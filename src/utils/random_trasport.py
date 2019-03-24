# -*- coding: utf-8 -*-

import random


def random_tra(second):
    li = []
    mo = second / 100.0
    for i in range(second):
        li.append(random.randint(0, 1))
    for i in range(len(li)):
        if i > 0:
            result_pre = i * li[i-1] / mo
            result_now = i * li[i] / mo
            if not result_now:
                result_now = result_pre
        else:
            result_now = i * li[i] / mo
        print("{0}%".format(result_now))


if __name__ == "__main__":
    random_tra(600)
