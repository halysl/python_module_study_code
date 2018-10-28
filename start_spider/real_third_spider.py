# -*- coding:utf-8 -*-
# author:light
# date:2018-10-28
# info:可用，但由于js限制，暂时使用本地保存文件
# slogan:狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。

# 选择目标：https://steamcn.com/f161-1

import logging
import logging.handlers
import os
import sys
import pdb

import requests
from lxml import html


curr_path = os.path.dirname(os.path.abspath(__file__))

def get_logger(level):
    # 生成日志文件名
    log_file_name = os.path.join(curr_path, "real_second_spider.log")  # 日志名
    # 创建logger记录器和输出格式
    logger_ = logging.getLogger("second-spider")
    logger_.setLevel(level)
    formatter = logging.Formatter('[%(name)s %(levelname)s %(asctime)s %(funcName)s %(module)s:%(lineno)d] %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    # 创建文件handler并设置输出格式
    log_file_handle = logging.handlers.RotatingFileHandler(log_file_name, maxBytes=10 * 1024 * 1024, backupCount=10)
    log_file_handle.setFormatter(formatter)

    logger_.addHandler(log_file_handle)

    return logger_


logger = get_logger(logging.INFO)

if __name__ == "__main__":
    with open('/Users/light/Downloads/aaaaa.htm', 'r') as f:
        date = f.read()
    tree = html.fromstring(date)

    date = []
    
    result = tree.xpath('///*[@id="threadlisttableid"]/tbody')
    
    for tbody in result:
        if tbody.xpath('@id')[0].startswith('stickthread'):
            result = tbody.xpath('tr/th/a[2]/text()')
        elif tbody.xpath('@id')[0].startswith('separatorline'):
            result = []
        elif tbody.xpath('@id')[0].startswith('normalthread'):
            result = tbody.xpath('tr/th/a/text()')
        else:
            result = tbody.xpath('tr/td[2]/a/text()')
        
        if result:
            date.extend(result)
    
    print date
