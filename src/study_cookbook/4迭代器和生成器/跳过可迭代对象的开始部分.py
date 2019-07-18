# -*- coding: utf-8 -*-
# 这个的原理和迭代器切片类似，通过itertools重新生成一个迭代器

from itertools import dropwhile


def skip_some_elec():
    with open('/etc/passwd') as f:
        # 可以看到dropwhile()的原型是dropwhile(func, 可迭代对象)
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line, end='')
