#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: 
# Desc: 
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""

from abc import ABCMeta, abstractmethod


class IStream():
    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self, maxbyte=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass

def serialize(stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


if __name__ == "__main__":
    try:
        i = IStream()
    except TypeError as e:
        print(e.message)

    i = SocketStream()
    print serialize(i)
