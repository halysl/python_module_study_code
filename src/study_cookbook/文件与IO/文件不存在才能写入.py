# -coding: utf-8 -*-
# 利用 open 方法的 x 模式替代 w 模式，仅限 python3


def just_write_file():
    with open('somefile', 'wt') as f:
        f.write('Hello\n')


def write_on_not_existed_file():
    with open('somefile', 'xt') as f:
        f.write('Hello\n')

if __name__ == "__main__":
    just_write_file()
    write_on_not_existed_file()
