#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: 
# Desc: 通过某个关键字排序一个字典列表
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


def sort_dictlist_by_keyword():
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

    # itemgetter接受一个关键字，返回可被排序的函数， 这样字典列表就可以根据key进行排序
    row_by_fname = sorted(rows, key=itemgetter('fname'))
    row_by_uid = sorted(rows, key=itemgetter('uid'))
    row_by_fname_and_uid = sorted(rows, key=itemgetter('fname', 'uid'))

    row_by_fname_lambda = sorted(rows, key=lambda r: r['fname'])
    row_By_uid_lambda = sorted(rows, key=lambda r: r['uid'])
    row_by_fname_and_uid_lambda = sorted(
        rows, key=lambda r: (r['fname'], r['uid']))

    assert row_by_fname == row_by_fname_lambda
    assert row_by_uid == row_By_uid_lambda
    assert row_by_fname_and_uid == row_by_fname_and_uid_lambda

    num_list = [
      [1, 3, 4, 5], 
      [4, 3, 1, 2], 
      [2, 5, 6, 3]
    ]
    # itemgetter接受一个整数，返回可被排序的函数， 这样列表的列表就可以根据index进行排序
    numlist_by_index0 = sorted(num_list, key=itemgetter(0))
    numlist_by_index1 = sorted(num_list, key=itemgetter(1))
    numlist_by_index0_and_index1 = sorted(num_list, key=itemgetter(0, 1))

    numlist_by_index0_lambda = sorted(num_list, key=lambda n: n[0])
    numlist_by_index1_lambda = sorted(num_list, key=lambda n: n[1])
    numlist_by_index0_and_index1_lambda = sorted(num_list, key=lambda n: (n[0], n[1]))

    assert numlist_by_index0 == numlist_by_index0_lambda
    assert numlist_by_index1 == numlist_by_index1_lambda
    assert numlist_by_index0_and_index1 == numlist_by_index0_and_index1_lambda



if __name__ == "__main__":
    sort_dictlist_by_keyword()
