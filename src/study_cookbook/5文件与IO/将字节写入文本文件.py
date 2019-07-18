# -*- coding: utf-8 -*-
# 仅在python3下有效，2和3的file部分差的太多


def example_buffer_write():
    path = "/tmp/temp"
    f = open(path, 'w')
    f.buffer.write(b"hello world")
    f.close()

    f = open(path, "r")
    data = f.read()
    f.close()

    print(data)

if __name__ == "__main__":
    example_buffer_write()
