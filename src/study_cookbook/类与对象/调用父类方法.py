# -*- coding: utf-8 -*-
# 在子类中调用父类的某个已经被覆盖的方法
# super 的使用相对比较复杂，会更新一篇文章说这个


class A(object):
    def __init__(self):
        self.x = 0

    def spam(self):
        print('A.spam')


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1

    def spam(self):
        print('B.spam')
        super().spam()  # Call parent spam()

if __name__ == "__main__":
    a = A()
    b = B()
    a.spam()
    b.spam()
    print(a.__dict__)
    print(b.__dict__)

    # 通过 mro 列表看super顺序，super本身就是个类
    print(A.__mro__)
    print(B.__mro__)
