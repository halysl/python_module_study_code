# -*- coding: utf-8 -*-
# 利用约定俗成的下划线实现私有属性或私有方法
# 有 前单下划线、前双下划线、后单下划线
# 后单下划线 和权限无关，只是防止定义的一个变量和某个保留关键字冲突
# 前单下划线
# 前双下划线 和继承有关


class A(object):
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        return "this is a public method"

    def _internal_method(self):
        return "this is a internal method"


class B(object):
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        return "this is a private method"

    def public_method(self):
        self.__private_method()

if __name__ == "__main__":
    a = A()
    print(a.__dict__)
    print(a.public_method())
    print(a._internal_method())
    print("可以看到都可以直接调用，所以需要约定俗成")

    b = B()
    print(b.__dict__)
    print("可以看到此时的变量 变为了_B__private，但是b._B__private = {}，依旧可以调用".format(
        b._B__private))
    print(dir(b))
    print("同时private私有方法变成了_B__private，那么b._B_private_method = {}".format(
        b._B__private_method()
    ))

    print("所以python本身没什么控制，只是看用的人怎么控制")
