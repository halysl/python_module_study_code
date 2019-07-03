# -*- coding: utf-8 -*-
# 通过将代码反编译成低级的字节码来查看它底层的工作机制
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p25_disassembling_python_byte_code.html

import dis


def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1
    print('Done!')

if __name__ == "__main__":
    countdown(10)
    print('\n')
    print(dis.dis(countdown))
