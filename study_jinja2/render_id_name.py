# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

from jinja2 import Environment, PackageLoader
env = Environment()

template = env.get_template('templates/form.html')

print template.render(item=[{'id': 1, 'name': 'Ash'}])