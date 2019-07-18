# -*- coding: utf-8 -*-
"""
第一种，你可以使用PYTHONPATH环境变量来添加
bash % env PYTHONPATH=/some/dir:/other/dir python3
Python 3.3.0 (default, Oct 4 2012, 10:17:33)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/some/dir', '/other/dir', ...]
>>>
"""

"""
第二种方法是创建一个.pth文件，将目录列举出来
# myapplication.pth
/some/dir
/other/dir
这个.pth文件需要放在某个Python的site-packages目录
通常位于/usr/local/lib/python3.3/site-packages
或者 ~/.local/lib/python3.3/sitepackages。当解释器启动时
.pth文件里列举出来的存在于文件系统的目录将被添加到sys.path。
安装一个.pth文件可能需要管理员权限，如果它被添加到系统级的Python解释器。
"""

"""
第三种，手动添加，不推荐
import sys
sys.path.insert(0, '/some/dir')
sys.path.insert(0, '/other/dir')

import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), 'src'))
"""
