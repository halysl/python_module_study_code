# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

# 准备一个基类（父类）
class BaseClass:
     def talk(self):
         print("i am people")
 
 # 准备一个方法
def say(self):
     print("hello")
 
# 使用type来创建User类
User = type("User", (BaseClass, object), {"name":"user", "say":say})

print(User)