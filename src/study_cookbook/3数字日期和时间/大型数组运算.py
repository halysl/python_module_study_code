# -*- coding: utf-8 -*-

"""
python原生对数组的计算支持的效果较差，可以使用numpy库
"""

import numpy as np


def create_a_matrix():
    ax = np.array([1, 2, 3, 4])
    ay = np.array({5, 6, 7, 8})

    print("ax={}\tay={}".format(ax, ay))
    print("ax + 2={}\nax * 2={}\nax + ax={}\n".format(ax+2, ax*2, ax+ax))
    print("sqrt(ax)={}\nsin(ax)={}\ncos(ax)={}".format(
        np.sqrt(ax), np.sin(ax), np.cos(ax)))

if __name__ == "__main__":
    create_a_matrix()
