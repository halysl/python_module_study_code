# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: 专为deepin linux设置壁纸，需要用户提供壁纸文件夹，需要python3

import os
import random

"""
TODO(halysl0817@gmail.com):Change the wallpaper by changing the time
利用linux下的crontab工具实现半小时切换一次，
*/30 * * * * python /xxx/changebackground.py
"""

# 更换壁纸指令，此为deepin更换指令，不代表所有linux发行版更换指令
cmd = "gsettings set com.deepin.wrap.gnome.desktop.background picture-uri "
# 图片目录，用户可自主更换
path = "/home/light/Documents/code/spider-on-lol/lolSpider/lolSpider/img/hero_skin_img/full/"

# 利用os.listdir()方法获取图片目录下的所有文件名的列表
pic_list = os.listdir(path)

# 确切的文件位置，以及确切的更换指令
real_path = ''.join([path, str(random.choices(pic_list))[2:-2]])
real_cmd = "{cmd} {path}".format(cmd, real_path)

# 执行
os.system(real_cmd)

