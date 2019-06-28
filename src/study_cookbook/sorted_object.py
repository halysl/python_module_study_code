#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName:
# Desc: 对对象的列表进行排序（根据对象的某些属性）
# Author: 刘志
# Email: halysl0817@gmail.com
# HomePage: ${link}
# Version: 0.0.1
# LastChange: 2018-11-28 15:24
# History:
# slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
#=============================================================================
"""
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sorted_object_by_lambda(objects):
    # 通过对象的user_id进行排序
    print sorted(objects, key=lambda u: u.user_id)


def sorted_object_by_attrgetter(objects):
    # 通过attrgetter的参数keyword 拿到对应的排序函数
    print sorted(objects, key=attrgetter('user_id'))


if __name__ == "__main__":
    users = [User(23), User(3), User(99)]
    print(users)

    sorted_object_by_lambda(users)
    sorted_object_by_attrgetter(users)
