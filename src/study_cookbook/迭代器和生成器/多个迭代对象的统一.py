# -*- coding: utf-8 -*-
# chain的使用

from itertools import chain


def example_chain():
    a = [1, 2, 3]
    b = ["a", "b", "c"]
    for x in chain(a, b):
        print(x)
    # 开销大，且a,b类型需要一致
    for x in a + b:
        print(x)

if __name__ == "__main__":
    example_chain()
