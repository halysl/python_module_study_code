import json
from docxtpl import DocxTemplate

doc = DocxTemplate("report_tpl_5_x.docx")

with open('ds.json', 'r') as f:
    data = json.load(f)

doc.render(data)
doc.save( "generated_doc.docx")