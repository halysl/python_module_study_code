# -*- coding:utf-8 -*-
# author:light
# date:
# info:一个真正，可用的爬虫
# slogan:狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。

# 选择目标：https://steamcn.com

import logging
import logging.handlers
import os
import sys
import pdb

import requests
from lxml import etree


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


def get_info(url, headers=None, flag=None):
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        r.encoding = 'utf-8'
    else:
        raise requests.RequestException

    if not flag:
        return r.text

def get_xml_info(context):
    html = etree.HTML(context)
    result = etree.tostring(html)
    return result


if __name__ == "__main__":
    try:
        url = 'https://steamcn.com'
        context = get_info(url)
        print get_xml_info(context)
    except requests.RequestException as e:
        logger.error(e.message)
        sys.exit(-1)
