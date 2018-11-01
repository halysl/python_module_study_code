# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

import doctest

def multiply(a, b):
    """
    >>> multiply(1, 4)
    4
    >>> multiply(0, 2)
    0
    >>> multiply(2, 0.5)
    1.0
    >>> multiply('a', 3)
    'aaa'
    >>> multiply(3, 'a')
    'aaa'
    >>> multiply('a', 0)
    ''
    """
    return a * b

if __name__ == "__main__":
    # 以下代码启动doctets，或者
    # 命令行下：python -B doctest -v *.py
    doctest.testmod(verbose=False)