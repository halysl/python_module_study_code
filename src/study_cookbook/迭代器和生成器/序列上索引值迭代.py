# -*- coding: utf-8 -*-
# enumerate() 的使用


def example_enumerate():
    li = ["a", "b", "c"]
    for index, value in enumerate(li):
        print("index={}\tvalue={}".format(index, value))
    for index, value in enumerate(li, 1):
        print("index={}\tvalue={}".format(index, value))


def core_enumerate():
    """
    >>> li = [(1,2),(3,4),(5,6)]
    >>> li
    [(1, 2), (3, 4), (5, 6)]
    >>> a = enumerate(li)
    >>> next(a)
    (0, (1, 2))
    >>> next(a)
    (1, (3, 4))
    >>> next(a)
    (2, (5, 6))
    >>>
    """
    pass

if __name__ == "__main__":
    example_enumerate()
