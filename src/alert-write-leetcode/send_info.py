# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime

import requests

dir_name = os.path.dirname(os.path.abspath(__file__))


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


def get_origin_info(data, today):
    return data.get(today, {})


def gene_markdown_info(info, today):
    dt = datetime.now()
    today = dt.strftime("%Y-%m-%d")
    weekly_dict = {
        0: "星期一",
        1: "星期二",
        2: "星期三",
        3: "星期四",
        4: "星期五",
        5: "星期六",
        6: "星期天"
        }
    week = weekly_dict.get(dt.weekday(), "星期未知")

    level_dict = {
        1: "<font color=\"info\">简单</font>",
        2: "<font color=\"comment\">中等</font>",
        3: "<font color=\"warning\">困难</font>"
    }
    level = level_dict.get(info["level"], "未知")

    problem = info["question__title"]
    url = info["question__url"]

    msg = ("测试（无@效果)\n"
           "## 群公告\n"
           "### 上班时间严禁刷题！！！刷题不能影响正常工作！！！\n"
           "### 上班时间严禁刷题！！！刷题不能影响正常工作！！！\n"
           "### 上班时间严禁刷题！！！刷题不能影响正常工作！！！\n\n"
           "### **今日份烧脑**\n"
           "> 日期：{today} {week}\n"
           "> 题目：[{problem}]({url})\n"
           "> 难度：{level}\n\n"
           "每天保证一道题，我会在早上更新群公告，代码可以提交到repl.it上，然后将链接贴到群里，这样可以互相看到对方的代码，互相学习\n"
           "刷题是完全自愿的，但为了给大家一点小小的压力，**一周内打卡不足3次**的同学会被暂时移出群，"
           "需要将一周的题目补齐才能重新进群\n".format(
               today=today, week=week, problem=problem, url=url, level=level))

    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": msg,
            "mentioned_list": [],
            "mentioned_mobile_list": ["@all"]
        }
    }

    return data

if __name__ == "__main__":
    today = datetime.now().strftime("%Y%m%d")
    today = "20190809"
    with open(os.path.join(dir_name, "problem_list"), "r") as f:
        data = json.load(f)
    info = get_origin_info(data, today)
    if info:
        markdown_request_info = gene_markdown_info(info, today)
        print(markdown_request_info)
    else:
        print("今天无题目")

    hook = ""
    requests.post(hook, json=markdown_request_info)
    # hook = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?{key}"
    # mentioned_mobile_list = []
    # create_hookinfo(hook, msg, mentioned_mobile_list)
