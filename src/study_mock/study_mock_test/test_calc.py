# -*-coding:utf-8 -*-

import unittest
import mock
from src.study_mock import Count


class TestCalc(unittest.TestCase):
    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value=13, side_effect=count.add)
        result = count.add(8, 5)
        self.assertEqual(result, 13)
