# -*- coding: utf-8 -*-

"""
从json文件渲染word文档
"""

from docxtpl import DocxTemplate, RichText
import json

with open('ds.json', 'r') as f:
    data = json.load(f)

doc = DocxTemplate("report_tpl_4_x.docx")
doc.render(data)
doc.save('result.doc')
