# -*- coding:utf-8 -*-
# 通过os.path 测试文件是否存在、类型、大小、修改时间等

import os
import time


def example_os_path():
    passwd = "/etc/passwd"
    python = "/usr/local/bin/python"
    print("/etc/passwd exists:{}\n/usr/local/bin/python exists:{}\n".format(
        os.path.exists(passwd),
        os.path.exists(python)
    ))
    print("/etc/passwd is file:{}\n/usr/local/bin/python is file:{}\n".format(
        os.path.isfile(passwd),
        os.path.isfile(python)
    ))
    print("/etc/passwd is dir:{}\n/usr/local/bin/python is dir:{}\n".format(
        os.path.isdir(passwd),
        os.path.isdir(python)
    ))
    print("/etc/passwd is link:{}\n/usr/local/bin/python is link:{}\n".format(
        os.path.islink(passwd),
        os.path.islink(python)
    ))
    print("/etc/passwd size:{}\n/usr/local/bin/python size:{}\n".format(
        os.path.getsize(passwd),
        os.path.getsize(python)
    ))
    print("/etc/passwd ctime:{}\n/usr/local/bin/python ctime:{}\n".format(
        os.path.getctime(passwd),
        os.path.getctime(python)
    ))
    print("/etc/passwd mtime:{}\n/usr/local/bin/python mtime:{}\n".format(
        time.ctime(os.path.getmtime(passwd)),
        time.ctime(os.path.getmtime(python))
    ))
if __name__ == "__main__":
    example_os_path()
