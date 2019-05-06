# -*- coding: utf-8 -*-
# 读取二进制数据到缓冲区，可以直接对缓冲区数据做修改

import os.path


def read_into_buffer(filename):
    # 先创建缓冲区
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        # 通过readinto方式将数据存进缓冲区
        f.readinto(buf)
    return buf


def use_the_buf():
    with open('sample.bin', 'wb') as f:
        f.write(b'Hello World')
    buf = read_into_buffer('sample.bin')
    print(buf[0:5])
    with open('newsample.bin', 'wb') as f:
        f.write(buf)


def example_memoryview():
    # 原地动刀子
    with open('sample.bin', 'wb') as f:
        f.write(b'Hello World')
    buf = read_into_buffer('sample.bin')
    print(buf)
    # 零复制的方式对已存在的缓冲区执行切片
    m1 = memoryview(buf)
    m1[-5:] = b"WORLD"
    print(buf)

if __name__ == "__main__":
    use_the_buf()
    example_memoryview()
