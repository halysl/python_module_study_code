# -*- coding: utf-8 -*-
# 通过json传递数据
import os
import json
path = os.path.dirname(__file__)


def example_json_dump():
    data = {"a": 1, "b": 2, "c": 3}
    # 将字典转为字符串
    data_dump = json.dumps(data)
    print("data={}\ndata_dump={}\ntype(data)={}\ntype(data_dump)={}".format(
        data, data_dump, type(data), type(data_dump)))
    # 将字典存入文件
    with open(os.path.join(path, "test.json"), "wt") as f:
        json.dump(data_dump, f)


def example_json_load():
    data = "{\"a\": 1, \"b\": 2, \"c\": 3}"
    data_load = json.loads(data)
    print("data={}\ndata_load={}\ntype(data)={}\ntype(data_load)={}\n".format(
        data, data_load, type(data), type(data_load)))
    with open(os.path.join(path, "test.json"), "rt") as f:
        data = json.load(f)
        print("data={}".format(data))

if __name__ == "__main__":
    print("json dump example：")
    example_json_dump()
    print("\njson load example:")
    example_json_load()
