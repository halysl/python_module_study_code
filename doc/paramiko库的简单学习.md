[TOC]
#paramiko库的简单学习
paramiko，一个听起来不像英语的库，在诸多英文名的库中独立旗帜（官方解释为："Paramiko" is a combination of the Esperanto words for "paranoid" and "friend"）。它的主要功能就是实现对ssh协议的封装，能够在一个更高层面上，轻松地使用ssh以及sftp等功能。
##一、安装
```python
pip install paramiko
```
##二、ssh连接对象
1.使用密码连接
```python
import paramiko
# 这行代码可以生成连接日志，大部分情况下不需要
# paramiko.util.log_to_file('/tmp/sshout')
ssh = paramiko.SSHClient()
#这行代码的作用是允许连接不在know_hosts文件中的主机。
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("IP", port, "username", "password")
```
2.使用秘钥连接
```python
import paramiko
ssh = paramiko.SSHClient()
ssh.connect('10.120.48.109', port, '用户名', key_filename='私钥')
```
##三、ssh执行指令
成功连接主机后，可以使用ssh.exec_command(cmd)的方法执行指令。
但默认返回三个paramiko.channelfile对象，我们可以用以下的方法读取数据或者写入确认等。
```python
stdin, stdout, stderr = ssh.exec_command(cmd)
# 如果成功，stdout会拿到输出的结果
for line in stdout.readlines():
    print(line)
# 执行过程中，可以使用以下方法进行确认，但此时的确认是对指令操作过程中的指令，例如“确认删除”等
stdin.write('Y')
# 执行过程中若出现错误信息，报错信息会保存在stderr中
```
##四、sftp对象
paramiko的sftp对象有多种生成方式。
倘若已有ssh对象，则：
- sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
- sftp = ssh.open_sftp()  # 推荐，简单
  倘若没有ssh对象，可以直接创建一个加密管道，开启传输。
```python
scp = paramiko.Transport(('ip', port))
scp.connect(username='username', password='password')
sftp = paramiko.SFTPClient.from_transport(scp)
```
##五、sftp相关操作
当已经创建了sftp对象，查看对象拥有的方法，发现会有很多，并且做了一定的封装，例如sftp.chown(),sftp.chmod()等方法，这些方法其实可以通过ssh.exec_command(cmd)的方法实现，但在这里可以明显的感受到：ssh对象面向的是主机，sftp对象面向的是文件系统。
几个常见的操作：
- sftp.get(remotepath, localpath, callback=None)  # 下载文件
- sftp.put(localpath, remotepath, callback=None, confirm=True) # 上传文件
- sftp.stat(path) # 查看文件状态

更多操作可见[sftp对象的方法](http://docs.paramiko.org/en/2.4/api/sftp.html)
##六、利用paramiko实现ssh的交互式连接
这样可以让我们在执行py文件的时候，连接到远端主机的shell，进行一定的操作，并且退出后脚本可以继续执行。
实现步骤：
1、连接远端主机
2、创建tty
3、执行一些指令
4、退出
5、脚本继续运行

创建一个文件，叫做interactive.py。
```python
import socket
import sys
# windows does not have termios...
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False
def interactive_shell(chan):
    if has_termios:
        posix_shell(chan)
    else:
        windows_shell(chan)
def posix_shell(chan):
    import select
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = chan.recv(1024)
                    if len(x) == 0:
                        print 'rn*** EOFrn',
                        break
                    sys.stdout.write(x)
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                if len(x) == 0:
                    break
                chan.send(x)
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
# thanks to Mike Looijmans for this code
def windows_shell(chan):
    import threading
    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.rnrn")
    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('rn*** EOF ***rnrn')
                sys.stdout.flush()
                break
            sys.stdout.write(data)
            sys.stdout.flush()
    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()
    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            chan.send(d)
    except EOFError:
        # user hit ^Z or F6
        pass
```

主脚本ssh_inter.py
```python
# -*- coding:utf-8 -*-
import paramiko
import interactive
# 记录日志
paramiko.util.log_to_file('/tmp/test')
# 建立ssh连接
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    '10.10.100.71',
    port=22,
    username='root',
    password='cljslrl0620',
    compress=True)
# 建立交互式shell连接
channel = ssh.invoke_shell()
# 建立交互式管道
interactive.interactive_shell(channel)
# 关闭连接
channel.close()
ssh.close()
```
终端执行python ssh_inter.py，可以看到效果。

这一段感谢[python模块paramiko与ssh](http://www.361way.com/python-paramiko-ssh/3984.html)。

同时需要注意，执行脚本的机器和远端机器的shell最好为一种shell，例如bash。

## 七、更多
[paramiko官方api文档](http://docs.paramiko.org/en/2.4/)
[python模块paramiko与ssh](http://www.361way.com/python-paramiko-ssh/3984.html)
[使用python的paramiko模块实现ssh与scp功能](http://mingxinglai.com/cn/2015/06/paramiko/)