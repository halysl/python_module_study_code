# -*- coding: utf-8 -*-

from datetime import datetime


def str_2_datetime(text):
    return datetime.strptime(text, "%Y-%m-%d")


def datetime_2_str(datetime_obj):
    return datetime.strftime(datetime_obj, "%A %B %d, %Y")


if __name__ == "__main__":
    print(str_2_datetime("2019-01-01"))
    print(str_2_datetime("2018-09-30"))
    date = datetime.now()
    print(date)
    print(datetime_2_str(date))
