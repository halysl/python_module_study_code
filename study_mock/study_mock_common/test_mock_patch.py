# -*- coding:utf-8 -*-
# author:light
# date:
# info:一个真正，可用的爬虫
# slogan:狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# valid:54uC6aOO6aqk6Zuo5YKs57q45Lye77yM5ri45Lq65rWq6L+55q2l5LiN5LyR77yM5aSp5Zyw5ruC5rKx5aaC5L2V5rih77yM6JOR6KGj6KSq5bC95Lu75rWK5rWB44CC

import mock
import pytest
import os
from common_func import func_t


def test_func1():
    num = func_t()
    assert num == '1234'

@mock.patch('common_func.func', return_value='1')
def test_func2(mock_func):
    num = mock_func()
    assert num == '1'

def test_func3():
    mock_func = mock.Mock(return_value='1')
    func_t = mock_func
    num = func_t()
    assert num == '1'

@mock.patch('common_func.func', return_value='1')
def test_func4(mock_func):
    mock_func.return_value = '1'
    num = func_t()
    assert num == '1'

