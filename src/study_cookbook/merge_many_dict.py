#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: 
# Desc: 合并多个字典或映射
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""
# only on python3
from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)