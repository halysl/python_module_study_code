#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from apscheduler.schedulers.background import BackgroundScheduler


def print_a(**data):
    print(data)

Get_Status_Schedule = BackgroundScheduler(timezone="Asia/Shanghai")
job = Get_Status_Schedule.add_job(print_a, "interval", seconds=5, kwargs={"a": 1,"b":2}, id="test")
job.pause()

def print_b():
    print("b")

test_Schedule = BackgroundScheduler(timezone="Asia/Shanghai")
test_Schedule.add_job(print_b, "interval", seconds=5)

def main():
    # 设计一个定时任务，每五分钟触发下 set_control_status
    Get_Status_Schedule.start()
    while 1:
        # do your stuff...
        time.sleep(10)
        job.modify(kwargs={"c": 3})
        time.sleep(10)
        job.pause()


if __name__ == "__main__":
    main()
