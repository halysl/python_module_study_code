# -*- coding: utf-8 -*-

import os
import sys
import errno
import unittest

dirpath = os.path.dirname(os.path.abspath(__file__))


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


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)

if __name__ == '__main__':
    with open(os.path.join(dirpath, 'testing.out'), 'w') as f:
        main(f)
