# -*- coding: utf-8 -*-
# 使用 abc

from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass

if __name__ == "__main__":
    s = SocketStream()
    print(s)
    print(SocketStream.__mro__)
