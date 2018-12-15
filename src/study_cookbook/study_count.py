#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: 
# Desc: 通过Counter类对可hash对象进行数量统计
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""
from copy import copy
from collections import Counter

if __name__ == "__main__":
    words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
    ]
    word_count = Counter(words)
    print word_count
    
    print word_count.most_common(3)

    word_count2 = copy(word_count)
    
    # Counter可以进行数学计算，对同样的key的value进行加减操作， 同样的也可以增加新的key-value
    print word_count2 + word_count
    print word_count2 - word_count