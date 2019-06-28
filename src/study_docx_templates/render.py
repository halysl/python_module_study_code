# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

from docxtpl import DocxTemplate, RichText

doc = DocxTemplate("my.docx")

context = dict()

# 常规渲染
context['company_name'] = "World company"

# 循环生成行
context['persons'] = [
    {'name': 'Ash', 'age': 18, 'status': 'ok'},
    {'name': 'Bob', 'age': 19, 'status': 'fail'},
    {'name': 'Cat', 'age': 20, 'status': 'fail'},
    {'name': 'Dis', 'age': 21, 'status': 'ok'},
    {'name': 'Eva', 'age': 22, 'status': 'fail'}
]

# 着上背景色
OK = GREEN = '#008000'
FAIL = RED = '#FF0000'
TODO = YELLOW = '#FFFF00'
DOING = CYAN = '#00FFFF'
DONE = BLUE = '#0000FF'

context['colors'] = [
    {'status': 'OK', 'color': 'GREEN', 'bgcolor': OK},
    {'status': 'FAIL', 'color': 'RED', 'bgcolor': FAIL},
    {'status': 'TODO', 'color': 'YELLOW', 'bgcolor': TODO},
    {'status': 'DOING', 'color': 'CYAN', 'bgcolor': DOING},
    {'status': 'DONE', 'color': 'BLUE', 'bgcolor': DONE}
]

# 渲染一个带有link的富文本
rt_link = RichText('You can add an hyperlink, here to ')
rt_link.add('google', url_id=doc.build_url_id('http://google.com'))
context['link'] = rt_link

# 渲染一个非主流文字颜色的富文本
rt_color = RichText()
rt_color.add(u'啊萨阿德\t', color=RED)
rt_color.add('GREEN\t', color=GREEN)
rt_color.add('YELLO\t', color=YELLOW)
rt_color.add('CYAN\t', color=CYAN)
rt_color.add('BLUE\t', color=BLUE)
context['word_color'] = rt_color

doc.render(context)
doc.save("generated_doc.docx")
