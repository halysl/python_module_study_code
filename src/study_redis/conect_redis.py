# -*- coding: utf-8 -*-
"""
redis 是一种 NoSQL， 它的数据有许多种类型，针对每种类型，对应的python-redis库有一套封装好的操作。
"""
import time
import redis

if __name__ == "__main__":
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
    r.set("a", "b")
    print(r["a"])
    print(r.get("a"))
    print(type(r))

    r.set("a", "1234", ex=3)
    print(r["a"])
    time.sleep(1)
    print(r["a"])
    time.sleep(3)
    print(r.get("a"))
