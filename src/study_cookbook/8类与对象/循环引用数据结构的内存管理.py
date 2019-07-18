# -*- coding: utf-8 -*-
# 由于python的数据引用机制，当两个对象互相有引用时，只删除一方并不能删掉，这会造成内存占用问题
# 通过对引用关系弱化来解决这个问题，即创建一个弱连接
# weakref

import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


def example_weak_ref():
    root = Node("root")
    c1 = Node("child")
    root.add_child(c1)
    print(root, root.children, root._parent)
    print(c1, c1.children, c1._parent)
    del root
    print(c1, c1.children, c1._parent)

if __name__ == "__main__":
    example_weak_ref()
