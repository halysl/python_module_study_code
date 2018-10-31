# -*- coding: utf-8 -*-
# @Date    : 2018-10-31 16:07:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: 类的__getitem__方法

class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __getitem__(self, key):
        # 以字典的方式调用
        return self.__dict__.get(key)

if __name__ == "__main__":
    a = A('Ash', '18')
    print(a.name)
    print(a['name'])