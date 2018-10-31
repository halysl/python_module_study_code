# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

from contextlib import contextmanager
import time

class File(object):
    def __init__(self, filename, method):
        self.fileobj = file(filename, method)
    
    def __enter__(self):
        return self.fileobj

    def __exit__(self, type, value, traceback):
        self.fileobj.close()

with File('test', 'a') as f:
    now = time.strftime('%a, %d %b %Y %H:%M:%S\n', time.localtime())
    f.write(now)

with File('test', 'r') as f:
    print f.read()

# with File('test', 'r') as f:
#     f.unknow_func()

@contextmanager
def o_file(filename, method):
    f = file(filename, method)
    yield f
    f.close()

with o_file('test', 'a') as f:
    now = time.strftime('%a, %d %b %Y %H:%M:%S\n', time.localtime())
    f.write(now)

with o_file('test', 'r') as f:
    print f.read()


