# -*- coding: utf-8 -*-
# ast的使用
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p24_parse_and_analyzing_python_source.html

import ast


ex = ast.parse('2 + 3*4 + x', mode='eval')
print(ex, '\n')
print(ast.dump(ex), '\n')

top = ast.parse('for i in range(10): print(i)', mode='exec')
print(top, '\n')
print(ast.dump(top), '\n')
