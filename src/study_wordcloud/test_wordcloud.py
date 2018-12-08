# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

from pyecharts import WordCloud
import json


def render():
    name = []  # 词条
    value = []  # 权重
    with open('data.json', 'r') as f:
        data = json.load(f)

    for k, v in data.items():
        name.append(k)
        value.append(int(v))

    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("Xia", name, value, shape='circle', word_size_range=[20, 100])
    wordcloud.render()

if __name__ == "__main__":
    render()
