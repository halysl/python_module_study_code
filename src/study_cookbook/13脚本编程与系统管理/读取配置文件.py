# -*- coding: utf-8 -*-
# 读取 ini 配置信息
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p10_read_configuration_files.html

from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')
print(cfg.sections())
print(cfg.get("installation", "library"))
print(cfg.getboolean('debug', 'log_errors'))
print(cfg.getint('server', 'port'))
print(cfg.getint('server', 'nworkers'))
