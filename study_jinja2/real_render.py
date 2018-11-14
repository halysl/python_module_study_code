# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

import json
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('jinja2_templates', 'templates'))

template = env.get_template('巡检结果概览.html')

with open('info.json', 'r') as f:
    data = json.load(f)

result = template.render(data)

with open('render_info.html', 'w') as f:
    f.write(result.encode("utf-8"))