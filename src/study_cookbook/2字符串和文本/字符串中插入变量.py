#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# 通过 format 替换
>>> s = '{name} has {n} messages.'
>>> s.format(name='Guido', n=37)
'Guido has 37 messages.'
>>>
"""

"""
# 通过 format_map 替换
>>> name = 'Guido'
>>> n = 37
>>> s.format_map(vars())
'Guido has 37 messages.'
>>>
"""

"""
# format_map 会调用对象的 __dict__
>>> class Info:
...     def __init__(self, name, n):
...         self.name = name
...         self.n = n
...
>>> a = Info('Guido',37)
>>> s.format_map(vars(a))
'Guido has 37 messages.'
>>>
"""

"""
# 防止key找不到
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

>>> s.format_map(safesub(vars()))
'Guido has {n} messages.'
>>>
"""
