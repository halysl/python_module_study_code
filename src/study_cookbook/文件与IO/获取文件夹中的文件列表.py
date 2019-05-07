# -*- coding: utf-8 -*-
# os.listdir的使用

import os
import glob


def example_os_list_dir():
    file_path = os.path.abspath(__file__)
    dirpath = os.path.dirname(file_path)
    list_dir = os.listdir(dirpath)
    print(list_dir)

    abspath = [os.path.join(dirpath, x) for x in list_dir]
    print(abspath)
    name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) 
                    for name in abspath]
    for name, size, mtime in name_sz_date:
        print("name:{}\tsize:{}\tmtime:{}\n".format(
            os.path.basename(name), size, mtime))

if __name__ == "__main__":
    example_os_list_dir()
