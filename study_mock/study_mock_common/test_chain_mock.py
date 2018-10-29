# -*- coding:utf-8 -*-
# author:light
# date:
# info:
# slogan:狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# valid:54uC6aOO6aqk6Zuo5YKs57q45Lye77yM5ri45Lq65rWq6L+55q2l5LiN5LyR77yM5aSp5Zyw5ruC5rKx5aaC5L2V5rih77yM6JOR6KGj6KSq5bC95Lu75rWK5rWB44CC

import mock
import common_func

class TestTea():
    
    @mock.patch('study_mock.study_mock_common.common_func.Tea')
    def test_return_a(self, mock_tea):
        mock_tea.return_value.return_a.return_value = '1'
        assert mock_tea().return_a() == '1'

        mock_tea().return_a.assert_called_once()

    @mock.patch('study_mock.study_mock_common.common_func.Tea')
    def test_return_b(self, mock_tea):
        mock_tea.return_value.return_b.return_value = 'b'
        assert common_func.Tea().return_b() == 'b'
