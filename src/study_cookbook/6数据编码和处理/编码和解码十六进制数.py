# -*- coding: utf-8 -*-
# 通过使用 binascii 完成十六进制数的编码解码

import binascii


def example_encode():
    s = b'hello'
    h = binascii.b2a_hex(s)
    print("s={}\nh={}".format(s, h))

    new_s = binascii.a2b_hex(h)
    print("h={}\nnew_s={}".format(h, new_s))

if __name__ == "__main__":
    example_encode()
