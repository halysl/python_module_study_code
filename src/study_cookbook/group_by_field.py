#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName:
# Desc: 通过某个字段将记录分组
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""
from operator import itemgetter
from itertools import groupby


def goupy_with_groupby(data):
    # 先排序
    data.sort(key=itemgetter('date'))
    # groupby方法会根据key返回元组，元组第一项是key的值，第二项是key值在的那些元素的集合
    # type(date) str
    # type(items) itertools._grouper
    for date, items in groupby(data, key=itemgetter('date')):
        print(date)
        for i in items:
            print ' ', i


def group_without_groupby(data):
    data.sort(key=lambda d: d['date'])
    default_date = 0
    # 遍历列表，若元素的date值不一致则建立新分组，若一致则连接在之前的分组
    for item in data:
        if item['date'] != default_date:
            print item['date']
            print ' ', item
            default_date = item['date']
        else:
            print ' ', item


if __name__ == '__main__':
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    goupy_with_groupby(rows)
    print '==========='
    group_without_groupby(rows)
