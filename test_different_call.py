# -*- coding:utf-8 -*-
# author:light
# date:
# info:调用一次后“销毁部分代码”
# slogan:狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# valid:54uC6aOO6aqk6Zuo5YKs57q45Lye77yM5ri45Lq65rWq6L+55q2l5LiN5LyR77yM5aSp5Zyw5ruC5rKx5aaC5L2V5rih77yM6JOR6KGj6KSq5bC95Lu75rWK5rWB44CC

import os

def fun1():
    print('1')

def fun2():
    print('2')

def fun3():
    file_path = os.path.abspath(__file__)
    result = []
    # 读取当前所有文件保存到list
    with open(file_path, 'r') as f:
        for line in f.readlines():
            result.append(line)
    # 遍历列表，对fun1()的调度注释掉
    for index, value in enumerate(result):
        if value.startswith('    fun1()'):
            result[index] = '#    fun1()\n'
    # 把列表内容全部写入当前文件
    with open(file_path, 'w') as f:
        for line in result:
            f.write(line)

if __name__ == "__main__":
    fun1()
    fun2()
    fun3()