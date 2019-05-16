# -*- coding: utf-8 -*-


def example_strggle_lambda():
    # lambda里的x实时获取
    x = 10
    a = lambda y: x + y
    x = 20
    b = lambda y: x + y
    print(a(10), b(10))


def example_define_lambda():
    # 在定义lambda的时候确定x的值
    x = 10
    a = lambda y, x=x: x + y
    x = 20
    b = lambda y, x=x: x + y
    print(a(10), b(10))


def another_example():
    funcs = [lambda x: x + n for n in range(5)]
    res = [x(0) for x in funcs]
    print(res)

    funcs = [lambda x, n=n: x + n for n in range(5)]
    res = [x(0) for x in funcs]
    print(res)


if __name__ == "__main__":
    example_strggle_lambda()
    example_define_lambda()
    another_example()
