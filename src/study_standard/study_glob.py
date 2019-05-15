# -*- coding: utf-8 -*-
import os
import glob

dir_path = os.path.dirname(os.path.abspath(__file__))
dir_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def example_glob():
    files = glob.glob(os.path.join(dir_path, "*.py"))
    print("当前文件夹为：{}\n目录下有文件:".format(dir_path))
    for file in files:
        print("{}".format(file))

if __name__ == "__main__":
    example_glob()
