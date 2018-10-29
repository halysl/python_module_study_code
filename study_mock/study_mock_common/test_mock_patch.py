# -*- coding:utf-8 -*-
# author:light
# date:
# info:一个真正，可用的爬虫
# slogan:狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# valid:54uC6aOO6aqk6Zuo5YKs57q45Lye77yM5ri45Lq65rWq6L+55q2l5LiN5LyR77yM5aSp5Zyw5ruC5rKx5aaC5L2V5rih77yM6JOR6KGj6KSq5bC95Lu75rWK5rWB44CC

import mock
import pytest
import os
import common_func


def test_func1():
    num = common_func.func()
    assert num == '1234'

@mock.patch('study_mock.study_mock_common.common_func.func')
def test_func2(mock_func):
    mock_func.return_value = '1'
    assert common_func.func() == '1'

