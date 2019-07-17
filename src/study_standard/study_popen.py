# -*- coding:utf-8 -*-
# author:light
# date:2018-10-24 11:56
# info:test popen
# slogan:狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。

from subprocess import Popen, PIPE

cmd = 'su - grid'
p = Popen(cmd, bufsize=1000, shell=True, close_fds=True,
          stdout=PIPE, stderr=PIPE, stdin=PIPE)
cmd2 = 'ls'
p.stdin.write(cmd2)
result = p.communicate()
print(result[0].replace('/x1b', ''))


cmd1 = 'su - grid'
p1 = Popen(cmd1, bufsize=1000, shell=True, close_fds=True, stdout=PIPE)
cmd2 = 'ls'
# PIPE相当于缓冲区
p2 = Popen(cmd2, bufsize=1000, shell=True, stdin=p1.stdout, stdout=PIPE)
out = p2.communicate()
print(out)
