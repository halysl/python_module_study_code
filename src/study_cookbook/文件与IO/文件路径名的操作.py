# -*- coding: utf-8 -*-
# os.path的使用

import os


def example_os_path():
    path = '/Users/beazley/Data/data.csv'
    print("origin name:{}\nbasename:{}\ndirname:{}\npath split:{}".format(
        path,
        os.path.basename(path),
        os.path.dirname(path),
        os.path.split(path)))

if __name__ == "__main__":
    example_os_path()
