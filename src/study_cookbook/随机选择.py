# -*- coding: utf-8 -*-

import random


def random_choice():
    values = [1, 2, 3, 5, 7, 9]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))


def random_shuffle():
    values = [1, 2, 3, 5, 7, 9]
    print("origin values={}".format(values))
    random.shuffle(values)
    print("shuffle values={}".format(values))


def diff_random():
    """
    random 模块使用 Mersenne Twister 算法来计算生成随机数。这是一个确定性算法， 但是你可以通过 random.seed() 函数修改初始化种子。
    """
    random.seed()  # Seed based on system time or os.urandom()
    random.seed(12345)  # Seed based on integer given
    random.seed(b'bytedata')  # Seed based on byte data

if __name__ == "__main__":
    random_choice()
    random_shuffle()
