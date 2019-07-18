# -*- coding: utf-8 -*-

"""
# mymodule.py
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def bar(self):
        print('B.bar')
"""

"""
目标：
mymodule/
    __init__.py
    a.py
    b.py

# a.py
class A:
    def spam(self):
        print('A.spam')

# b.py
from .a import A
class B(A):
    def bar(self):
        print('B.bar')

# __init__.py
from .a import A
from .b import B
"""


"""
调用：
>>> import mymodule
>>> a = mymodule.A()
>>> a.spam()
A.spam
>>> b = mymodule.B()
>>> b.bar()
B.bar
>>>
"""
