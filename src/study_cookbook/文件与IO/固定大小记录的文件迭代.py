# -*- coding: utf-8 -*-

from functools import partial


def example_open():
    """
    iter() 函数有一个鲜为人知的特性就是，如果你给它传递一个可调用对象和一个标记值，它会创建一个迭代器。
    这个迭代器会一直调用传入的可调用对象直到它返回标记值为止，这时候迭代终止。
    在例子中， functools.partial 用来创建一个每次被调用时从文件中读取固定数目字节的可调用对象。
    标记值 b''就是当到达文件结尾时的返回值。
    """
    RECORD_SIZE = 32
    with open('somefile.data', 'rb') as f:
        records = iter(partial(f.read, RECORD_SIZE), b'')
        for r in records:
            print(r)

if __name__ == "__main__":
    example_open()
