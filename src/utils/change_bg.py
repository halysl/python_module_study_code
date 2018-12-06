# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: 专为deepin linux设置壁纸，需要用户提供壁纸文件夹，需要python3

import os
import random

# 利用linux下的crontab工具实现半小时切换一次，
# */30 * * * * python /xxx/changebackground.py

def change_bg(path):
    """deepin linux自动切换壁纸的方法"""
    # 更换壁纸指令，此为deepin更换指令，不代表所有linux发行版更换指令
    cmd = "gsettings set com.deepin.wrap.gnome.desktop.background picture-uri "
    # 利用os.listdir()方法获取图片目录下的所有文件名的列表
    # todo 可以递归的取
    pic_list = os.listdir(path)
    # 确切的文件位置，以及确切的更换指令
    random_pic = str(random.choices(pic_list))
    real_path = os.path.join([path, random_pic])
    real_cmd = "{cmd} {path}".format(cmd, real_path)

    os.system(real_cmd)
    return True

if __name__ == "__main__":
    # 图片目录，用户可自主更换
    path = "/home/light/Documents/code/spider-on-lol/lolSpider/lolSpider/img/hero_skin_img/full/"
    result = change_bg(path)
    print(result)
