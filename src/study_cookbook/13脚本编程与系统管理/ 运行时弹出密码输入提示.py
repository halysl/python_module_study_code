# -*- coding: utf-8 -*-

import getpass


def svc_login(user, passwd):
    print(user, passwd)
    default_dict = {"light": "dl"}
    return default_dict.get(user, "") == passwd


def check_up():
    # user = input('Enter your username: ')
    # 下面的代码会直接默认当前用户是user，而上方则是拿到一个输入值
    user = getpass.getuser()
    passwd = getpass.getpass()
    if svc_login(user, passwd):
        print("成功登陆！")
    else:
        print("不正确的账号/密码")

check_up()
