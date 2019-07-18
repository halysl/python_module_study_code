# -*- coding utf-8 -*-
import os
from xml.etree.ElementTree import parse, Element

"""
修改一个XML文档结构是很容易的，但是你必须牢记的是所有的修改都是针对父节点元素，
将它作为一个列表来处理。例如，如果你删除某个元素，通过调用父节点的remove()方法从它的直接父节点中删除。
如果你插入或增加新的元素，你同样使用父节点元素的 insert() 和 append() 方法。
还能对元素使用索引和切片操作，比如 element[i] 或 element[i:j]

如果你需要创建新的元素，可以使用本节方案中演示的 Element 类。我们在6.5小节已经详细讨论过了。
"""

path = os.path.dirname(__file__)


def example_modify_xml():
    doc = parse(os.path.join(path, "pred.xml"))
    root = doc.getroot()
    print(root)
    print(root.getchildren().index(root.find('pre')))
    root.remove(root.find('sri'))
    root.remove(root.find("cr"))
    print(root.getchildren().index(root.find('pre')))
    e = Element('spam')
    e.text = 'This is a test'
    root.insert(2, e)
    doc.write(os.path.join(path, "newpred.xml"), xml_declaration=True)

if __name__ == "__main__":
    example_modify_xml()
