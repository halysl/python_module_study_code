# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$
# 选择目标：https://steamcn.com

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
    log_file_name = os.path.join(curr_path, "spider.log")  # 日志名
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
    tree = html.fromstring(context)
    return tree

def parse_info(xml_parse):
    result = xml_parse.xpath('//*[@id="wp"]/div[2]/div[2]/div[1]/div[2]/div[1]/a/@href')
    return result

def parse_info2(xml_parse):
    result = xml_parse.xpath('//*[@id="threadlisttableid"]')
    print result

if __name__ == "__main__":
    try:
        url = 'https://steamcn.com'
        context = get_info(url)
        xml_parse = get_xml_info(context)
        next_url = parse_info(xml_parse)[0]
        next_url = ''.join([url, next_url])
        
        context = get_info(url)
        xml_parse = get_xml_info(context)
        parse_info2(xml_parse)
    except requests.RequestException as e:
        logger.error(e.message)
        sys.exit(-1)
