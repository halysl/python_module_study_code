# -*- coding: utf-8 -*-
# @Date    : 2018-10-31 16:02:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: 类的__getattr__ __getattribute__方法

class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, item):
        """
        该方法实现object.item的调用
        """
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        """
        当__getattribute__无法获取正确的属性时，调用该方法
        """
        return 'Default'

    def __setattr__(self, key, value):
        # self.__dict__保存着当前对象的所有属性，通过字典的方式调用
        self.__dict__[key] = value

if __name__ == "__main__":
    a = A('Ash', 18)
    
    print(a.name)
    print(a.__dict__.get('name'))
    print(a.__dict__['name'])
    print(a.__getattribute__('name'))

    a.name = 'Bob'
    print(a.name)
    a.__setattr__('name', 'Crs')
    print(a.name)

    print(a.undefined)