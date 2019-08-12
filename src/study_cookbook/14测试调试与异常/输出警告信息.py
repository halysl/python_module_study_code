# -*- coding: utf-8 -*-

import warnings


def func(x, y, logfile=None, debug=False):
    if logfile is not None:
        warnings.warn('logfile argument deprecated', DeprecationWarning)

func(1, 2, 3)

# python3 -W all 输出警告信息.py  # 输出所有警告
# python3 -W ignore 输出警告信息.py  # 忽略所有警告
# python3 -W error 输出警告信息.py  # 将警告转换为error

# 另一种控制警告的方式，是在代码里warnings.simplefilter()控制
# warnings.simplefilter('always')
# warnings.simplefilter('ignore')
# warnings.simplefilter('error')
