# -*- coding: utf-8 -*-
# 使用imp.reload()来重新加载先前加载的模块。

# reload()没有更新像”from module import name”这样使用import语句导入的定义。
# 少在生产环境用重新加载，会导致奇怪的问题
"""
>>> import spam
>>> import imp
>>> imp.reload(spam)
<module 'spam' from './spam.py'>
>>>
"""
