# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

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
