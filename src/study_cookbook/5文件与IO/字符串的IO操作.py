# -*- coding: utf-8 -*-
# 将一个文本或二进制字符串当作文件来使用
import io


def create_string_ip():
    s = io.StringIO()
    s.write('Hello World\n')
    # print 重定向到flie里
    print('This is a test', file=s)
    print(s.getvalue())

    s = io.StringIO('Hello\nWorld\n')
    print(s.read(4))
    print(s.read())

# io.StringIO 只能用于文本。如果你要操作二进制数据，要使用 io.BytesIO 类来代替。
if __name__ == "__main__":
    create_string_ip()
