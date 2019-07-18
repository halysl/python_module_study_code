# -*- coding: utf-8 -*-

"""
如果你想要合并的字符串是在一个序列或者 iterable 中，那么最快的方式就是使用 join() 方法。
"""

"""
>>> parts = ['Is', 'Chicago', 'Not', 'Chicago?']
>>> ' '.join(parts)
'Is Chicago Not Chicago?'
>>> ','.join(parts)
'Is,Chicago,Not,Chicago?'
>>> ''.join(parts)
'IsChicagoNotChicago?'
>>>
"""
