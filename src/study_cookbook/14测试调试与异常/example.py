# -*- coding: utf-8 -*-
from urllib.request import urlopen
import csv


def url_print(protocol, host, domain):
    url = f"{protocol}://{host}.{domain}"
    print(url)


def func(*args, **kwargs):
    pass


def dowprices():
    u = urlopen('http://finance.yahoo.com/d/quotes.csv?s=@^DJI&f=sl1')
    lines = (line.decode('utf-8') for line in u)
    rows = (row for row in csv.reader(lines) if len(row) == 2)
    prices = {name: float(price) for name, price in rows}
    return prices
