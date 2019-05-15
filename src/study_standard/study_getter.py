# -*- coding: utf-8 -*-


class A():
    attr1 = "test"

    def __init__(self):
        self.attr2 = "test2"
        self.attr3 = "test3"


def example_getter():
    a = A()
    print("a为{}\ntype(a) ==> {}\na.__dict__={}".format(a, type(a), a.__dict__))
    print("getattr(a, 'attr1') ==> {}".format(getattr(a, "attr1")))
    print("getattr(a, 'attr2') ==> {}".format(getattr(a, "attr2")))
    print("getattr(a, 'attr3') ==> {}".format(getattr(a, "attr3")))


def example_setter():
    a = A()
    print("a为{}\ntype(a) ==> {}\na.__dict__={}".format(a, type(a), a.__dict__))
    print("将会把attr1、attr2、attr3再次赋值")
    setattr(a, "attr1", 123)
    setattr(a, "attr2", 456)
    setattr(a, "attr3", 789)
    print("setattr(a, 'attr1', 123) ==> {}".format(a.attr1))
    print("setattr(a, 'attr2', 456) ==> {}".format(a.attr2))
    print("setattr(a, 'attr3', 789) ==> {}".format(a.attr3))


def example_delattr():
    a = A()
    print("a为{}\ntype(a) ==> {}\na.__dict__={}".format(a, type(a), a.__dict__))
    print("如果有attr2属性，则将其删除")
    if hasattr(a, "attr2"):
        delattr(a, "attr2")
    print("a为{}\ntype(a) ==> {}\na.__dict__={}".format(a, type(a), a.__dict__))

if __name__ == "__main__":
    example_getter()
    example_setter()
    example_delattr()
