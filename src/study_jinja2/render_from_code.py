# -*- coding: utf-8 -*-
# @Date    : 2018-11-09 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$


from jinja2 import Template

template = Template('Hello {{ name }}!')
result = template.render(name='John Doe')

print(result)
