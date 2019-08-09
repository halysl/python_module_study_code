# -*- coding: utf-8 -*-

import os

sz = os.get_terminal_size()


print(sz, '\n', sz.columns, '\n', sz.lines)
