# -*-coding:utf-8 -*-


class T(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'name:%s age:%s' % (self.name, self.age)


class S(object):
    # slots锁定当前类允许有的属性
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'name:%s age:%s' % (self.name, self.age)
