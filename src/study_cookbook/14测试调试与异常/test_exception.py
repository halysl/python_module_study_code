# -*- coding: utf-8 -*-
import errno
import unittest


def parse_int(x):
    return int(x)


class TestRaise(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')

    def test_detail_error(self):
        try:
            f = open("a")
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail("IOError not raised.")

if __name__ == "__main__":
    unittest.main()
