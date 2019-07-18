# -*- coding： utf-8-*-
import os
from xml.etree.ElementTree import Element, tostring

path = os.path.dirname(__file__)


def example_dict_2_xml(tag, d):
    elem = Element(tag)
    for k, v in d.items():
        child = Element(k)
        child.text = str(v)
        elem.append(child)
    return elem

if __name__ == "__main__":
    s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
    elem = example_dict_2_xml("storage", s)
    print(elem)
    print(dir(elem))
    print(tostring(elem))
    # 添加元素的属性
    elem.set("id", "1")
    print(tostring(elem))
    # 添加元素的属性
    elem.find("name").set("id", "2")
    print(tostring(elem))
