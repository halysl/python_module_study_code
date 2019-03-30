#!/usr/bin/env python
# -*- coding:utf-8 -*-

def a_wrong_example():
    # 在Unicode中，某些字符能够用多个合法的编码表示
    s1 = "Spicy Jalape\u00f1o"
    s2 = "Spicy Jalapen\u0303o"
    # false
    return s1 == s2
    # 这里的文本”Spicy Jalapeño”使用了两种形式来表示。 第一种使用整体字符”ñ”(U+00F1)，第二种使用拉丁字母”n”后面跟一个”~”的组合字符(U+0303)。
    # 在需要比较字符串的程序中使用字符的多种表示会产生问题。

def a_right_example():
    import unicodedata
    s1 = "Spicy Jalape\u00f1o"
    s2 = "Spicy Jalapen\u0303o"
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    # true
    print(t1 == t2)
    t3 = unicodedata.normalize('NFD', s1)
    t4 = unicodedata.normalize('NFD', s2)
    # true
    print(t3 == t4)
    # normalize() 第一个参数指定字符串标准化的方式。 
    # NFC表示字符应该是整体组成(比如可能的话就使用单一编码)，
    # 而NFD表示字符应该分解为多个组合字符表示。


