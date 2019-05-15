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


def example_yml_write():
    data = {"a": 1, "b": 2, "c": [1, 2, 3], "d": {"e": "test", "f": "test2",
            "g": [1, 0, 2, 4]}}
    with open(os.path.join(path, "write_yaml.yml"), "w") as f:
        yaml.dump(data, f)

if __name__ == "__main__":
    example_yml()
    example_yml_without_waring()
    example_yml_write()
