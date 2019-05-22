# -*- coding: utf-8 -*-
# 利用 collections的抽象类实现
# python3.8 之后，推荐用 collections.abc 导入集合抽象类

import bisect
import collections.abc as ca


class SortedItems(ca.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)

if __name__ == "__main__":
    items = SortedItems([5, 1, 3])
    print(list(items))
    print(items[0], items[-1])
    items.add(2)
    print(list(items))
    res = [isinstance(items, ca.Iterable),
           isinstance(items, ca.Sequence),
           isinstance(items, ca.Container),
           isinstance(items, ca.Sized),
           isinstance(items, ca.Mapping)]
    print(SortedItems.__mro__)

    print("Iterable\tSequence\tContainer\tSized\tMapping")
    print(res)

    print(len(items))
