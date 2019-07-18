# -*- coding: utf-8 -*-


def print_2_file():
    with open('/tmp/test.txt', 'wt') as f:
        print('Hello World!', file=f)
    with open('/tmp/test.txt', 'a+') as f:
        print('Hello World! --', file=f)

if __name__ == "__main__":
    print_2_file()
