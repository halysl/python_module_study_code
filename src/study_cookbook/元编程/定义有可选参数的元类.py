# -*- coding: utf-8 -*-
# __prepare__() 方法在所有类定义开始执行前首先被调用，用来创建类命名空间。 通常来讲，这个方法只是简单的返回一个字典或其他映射对象。
# __new__() 方法被用来实例化最终的类对象。它在类的主体被执行完后开始执行。
# __init__() 方法最后被调用，用来执行其他的一些初始化工作。
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p15_define_metaclass_that_takes_optional_arguments.html


class MyMeta(type):
    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Custom processing
        pass
        return super().__prepare__(name, bases)

    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        pass
        return super().__new__(cls, name, bases, ns)

    # Required
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        pass
        super().__init__(name, bases, ns)
