# -*- coding: utf-8 -*-

from datetime import timedelta
from datetime import datetime


def example_timedelta():
    # 两天六小时
    a = timedelta(days=2, hours=6)
    # 四点五个小时
    b = timedelta(hours=4.5)

    print("a have {} days {} hours\nb have {} days {} hours".format(
        a.days, a.seconds / 3600, b.days, b.seconds / 3600))
    c = a + b
    print("一共的天数：{0}\n除去{0}后有{1}秒，也就是{2}小时\n一共有{3}秒，也就是{4}小时".format(
        c.days,
        c.seconds,
        c.seconds / 3600,
        c.total_seconds(),
        c.total_seconds() / 3600))


def example_datetime():
    a = datea = datetime(2012, 9, 23)
    print(a + timedelta(days=10))

    b = datetime(2012, 12, 21)
    d = b - a
    print(d.days)

    now = datetime.today()
    print(now)
    print(now + timedelta(minutes=10))

if __name__ == "__main__":
    example_timedelta()
    example_datetime()
