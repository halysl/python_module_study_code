# -*- coding: utf-8 -*-
# @Date    : 2018-11-06 09:51:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: 调用父类方法构造函数

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.identity = 'Person'
    
    def eat(self):
        print('{} {} eat!'.format(self.identity, self.name))
    
    def birth(self):
        print('{} birth in year {}'.format(self.name, 2018-int(self.age)))


class Student(Person):
    def __init__(self, name, age):
        # super方法调用父类方法，参数为当前类名和self
        # 相当于 ParentClassName.method()
        super(Student, self).__init__(name, age)
        self.identity = 'Student'
    
    def yiqihecheng(self):
        super(Student, self).eat()
        super(Student, self).birth()


if __name__ == "__main__":
    p = Person('Ash', 18)
    p.eat()
    p.birth()
    s = Student('light', 17)
    s.yiqihecheng()
