# -*- coding: utf-8 -*-
# 使用 pandas

import os
import pandas

path = os.path.dirname(__file__)
file_path = os.path.join(path, "test2.csv")


def example_pandas():
    data = pandas.read_csv(file_path, skipfooter=1)
    print(data)
    print(dir(data))

if __name__ == "__main__":
    example_pandas()
