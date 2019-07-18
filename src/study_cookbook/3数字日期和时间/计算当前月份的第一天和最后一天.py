# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    # 先 生成一个date对象
    if not start_date:
        start_date = date.today().replace(day=1)
    else:
        start_date.replace(day=1)
    # 通过calendar.monthrange()确定当前日期所在的月份有多少星期和多少天
    weeks_on_month, days_on_month = calendar.monthrange(
        start_date.year, start_date.month)
    end_data = start_date + timedelta(days=days_on_month)
    return (start_date, end_data)

if __name__ == "__main__":
    a_day = timedelta(days=1)
    start_date, end_date = get_month_range()
    while start_date < end_date:
        print(start_date)
        start_date += a_day
