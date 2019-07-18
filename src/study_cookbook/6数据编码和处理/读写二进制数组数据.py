# -*- coding: utf-8 -*-
# 读写一个二进制数组的结构化数据到Python元组
import os
from struct import Struct

file_path = os.path.join(os.path.dirname(__file__), "data.b")


def write_records(records, f, format="<idd"):
    # 开一个结构体文件，对元组每一项分别添加
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


def read_records(f, format="<idd"):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)

if __name__ == "__main__":
    records = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    with open(file_path, 'wb') as f:
        write_records(records, f, "<idd")
    with open(file_path, 'rb') as f:
        for rec in read_records(f, '<idd'):
            print(rec)
