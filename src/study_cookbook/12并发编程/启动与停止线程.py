# -*- coding: utf-8 -*-
import time
from datetime import datetime
from threading import Thread


def long_task(n):
    while n >= 0:
        print(f"{datetime.strftime(datetime.now(), '%H:%M:%S')} number is {n}")
        n -= 1
        time.sleep(2)

if __name__ == "__main__":
    t = Thread(target=long_task, args=(4,))
    t.start()
    t.join()
