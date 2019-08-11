# -*- coding: utf-8 -*-
# 也就是对单个模块（单个py文件）配置一个独立的logger
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p12_add_logging_to_libraries.html

import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def func():
    logger.critical('A Critical Error!')
    logger.debug('A debug message')


func()
