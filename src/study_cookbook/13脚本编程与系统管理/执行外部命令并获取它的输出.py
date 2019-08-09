# -*- coding: utf-8 -*-
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p06_executing_external_command_and_get_its_output.html
# 执行一个外部命令并以Python字符串的形式获取执行结果

import subprocess


def most_simple_run_cmd():
    # 最简单方案
    out_bytes = subprocess.check_output(['ls', '-a'])
    out_text = out_bytes.decode('utf-8')
    print(out_bytes)
    print(out_text)


def run_cmd_with_error():
    try:
        out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'],
                                            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        out_bytes = e.output       # Output generated before error
        code = e.returncode   # Return code
