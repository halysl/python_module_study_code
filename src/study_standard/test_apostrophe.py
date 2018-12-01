# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: 单引号问题，后面会加上json相关的

a = {"a": 1}
print(a)
# {'a':11}, not {"a": 1}

b = {"a": {"b": 1}}
print(b)
# {'a': {'b': 1}}, not {"a":{"b":1}}
