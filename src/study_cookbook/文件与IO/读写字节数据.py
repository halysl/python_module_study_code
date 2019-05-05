# -*- coding: utf-8 -*-
# 使用 rb/wb 模式进行字节数据的读写


def example_read_byte_data():
    with open('somefile.bin', 'rb') as f:
        data = f.read()
    # Write binary data to a file
    with open('somefile.bin', 'wb') as f:
        f.write(b'Hello World')


def example_encode_decode():
    with open('somefile.bin', 'rb') as f:
        data = f.read(16)
        text = data.decode('utf-8')

    with open('somefile.bin', 'wb') as f:
        text = 'Hello World'
        # .encode('utf-8')指的是原文本格式为utf-8，现在加密为 byte 数据
        f.write(text.encode('utf-8'))
