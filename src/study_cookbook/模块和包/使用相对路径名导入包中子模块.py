# -*- coding: utf-8 -*-

"""
mypackage/
    __init__.py
    A/
        __init__.py
        spam.py
        grok.py
    B/
        __init__.py
        bar.py
"""

"""
现在在spam.py文件里
from . import grok
from ..B import bar

上面等于
from mypackage.A import grok
from mypackage.B import bar
"""
