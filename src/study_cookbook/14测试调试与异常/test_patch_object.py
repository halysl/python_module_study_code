# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock
import io

import example


"""
>>> x = 42
>>> with patch('__main__.x'):
...     print(x)
...
<MagicMock name='x' id='4314230032'>
>>> x
42
>>>
"""

"""
>>> x
42
>>> with patch('__main__.x', 'patched_value'):
...     print(x)
...
patched_value
>>> x
42
>>>
"""


class TestPatchObject(TestCase):
    @patch("example.func")
    def test1(self, mock_func):
        example.func(3)
        mock_func.assert_called_with(3)

    def test2(self):
        with patch('example.func') as mock_func:
            example.func(3)      # Uses patched example.func
            mock_func.assert_called_with(3)

    def test3(self):
        p = patch('example.func')
        mock_func = p.start()
        example.func(3)
        mock_func.assert_called_with(3)
        p.stop()

    def test_magic_mock_called(self):
        m = MagicMock()
        m.return_value = 10
        assert m(1, 2, debug=True) == 10
        m.assert_called_with(1, 2, debug=True)
        m.assert_called_with(1, 2)

    def test_magic_mock_define_method(self):
        m = MagicMock()
        m.upper.return_value = "HELLO"
        assert m.upper("hello") == "HELLO"

        m.split.return_value = ['hello', 'world']
        assert m.split('hello world') == ['hello', 'world']

    @patch("example.urlopen", return_value=io.BytesIO(b'''\
"IBM",91.1\r
"AA",13.25\r
"MSFT",27.72\r
\r
'''))
    def test_dowprices(self, mock_urlopen):
        p = example.dowprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p,
                         {'IBM': 91.1,
                          'AA': 13.25,
                          'MSFT': 27.72})


if __name__ == "__main__":
    unittest.main()
