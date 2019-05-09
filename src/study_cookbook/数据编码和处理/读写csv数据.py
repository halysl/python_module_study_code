# -*- coding: utf-8 -*-
# 通过csv模块读写

import os
import csv

path = os.path.dirname(__file__)


def example_csv_read():
    with open(os.path.join(path, "test.csv")) as f:
        f_csv = csv.reader(f)
        print("f_csv={}\ntype(f_csv)={}\n".format(f_csv, type(f_csv)))
        headers = next(f_csv)
        print("f_csv_header is {}".format(headers))

        info = list()
        for row in f_csv:
            default_dict = dict().fromkeys(headers)
            for index, (k, v) in enumerate(default_dict.items()):
                default_dict[k] = row[index]
            info.append(default_dict)
        print(info)


def example_csv_read2():
    with open(os.path.join(path, "test.csv")) as f:
        f_csv = csv.DictReader(f)
        info = [dict(x) for x in f_csv]
        print(info)


def example_csv_write():
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000)
            ]

    with open('stocks.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


def example_csv_write2():
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
            'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
            {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
            'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
            {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
            'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
            ]

    with open('stocks.csv', 'w') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)

if __name__ == "__main__":
    example_csv_read()
    example_csv_read2()
    example_csv_write()
    example_csv_write2()
