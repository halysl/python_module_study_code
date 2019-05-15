# -*- coding:utf-8 -*-
# 使用 base64 模块完成

import base64


def example_base64_encode():
    s = b"hello"
    encode = base64.b64encode(s)
    encode_2_str = base64.b64encode(s).decode("ascii")
    print("origin symbol is:{}\n"
          "base64 encode result:{}\n"
          "base64 encode to str result:{}\n"
          "type(origin):{}\t"
          "type(base64encode):{}\t"
          "type(base64encode2str):{}".format(
              s, encode, encode_2_str,
              type(s), type(encode), type(encode_2_str)))

if __name__ == "__main__":
    example_base64_encode()
