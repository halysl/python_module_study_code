# -*- coding: utf-8 -*-
import os
import yaml

path = os.path.dirname(__file__)
file_path = os.path.join(path, "test.yml")


def example_yml():
    with open(file_path, "r") as f:
        data = yaml.load(f)
    print(data)


def example_yml_without_waring():
    with open(file_path, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

if __name__ == "__main__":
    example_yml()
    example_yml_without_waring()
