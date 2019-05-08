# -*- coding: utf-8 -*-
# 通过pickle实现对象的序列化

import pickle

path = "/tmp/s.txt"


def example_pickle():
    data = [1, 2, 3, 4, 5]
    with open(path, 'wb') as f:
        # 序列化
        pickle.dump(data, f)
        s = pickle.dumps(data)
    print(s)
    with open(path, 'rb') as f:
        # print(f.read())
        # 反序列化
        new_data = pickle.load(f)
        print(new_data)


def example_more_pickle():
    f = open(path, 'wb')
    pickle.dump([1, 2, 3, 4], f)
    pickle.dump('hello', f)
    pickle.dump({'Apple', 'Pear', 'Banana'}, f)
    f.close()
    f = open(path, 'rb')
    res1 = pickle.load(f)
    res2 = pickle.load(f)
    res3 = pickle.load(f)
    print(res1, res2, res3, sep="\n")

if __name__ == "__main__":
    example_pickle()
    example_more_pickle()
