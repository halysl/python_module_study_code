# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

class Student(object):
    """
    >>> s = Student(18, 70)
    >>> s._age
    18
    >>> s._score
    70
    >>> s.age
    18
    >>> s.score
    70
    >>> s.age = -1
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "test_property.py", line 28, in age
        raise ValueError('请输入正确的年龄')
    ValueError: 请输入正确的年龄
    """
    def __init__(self, age, score):
        self._age = age
        self._score = score
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0 or age > 120:
            raise ValueError('请输入正确的年龄')
        self._age = age
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('请输入正确的年龄')
        self._score = score