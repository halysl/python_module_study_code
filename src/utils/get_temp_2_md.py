# -*- coding: utf-8 -*-
# 获得天气信息并推送
import requests


def create_hookinfo(hook, msg, mentioned_mobile_list):
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": msg,
            "mentioned_list": [],
            "mentioned_mobile_list": mentioned_mobile_list
        }
    }
    requests.post(hook, json=data)

if __name__ == "__main__":
    msg = ("今天是<font color=\"warning\">2019年7月26日</font>，星期五\n"
           ">距离下一次假期**中秋节**还有<font color=\"info\">49</font>天\n"
           ">距离2020年还有<font color=\"info\">159</font>天\n"
           ">`import this`")

    key = ""
    hook = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?{key}"
    mentioned_mobile_list = []
    create_hookinfo(hook, msg, mentioned_mobile_list)
