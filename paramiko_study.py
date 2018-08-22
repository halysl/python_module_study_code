#!/usr/bin/env python
# -*-coding:utf8-*-

import paramiko

# 创建ssh连接对象
ssh = paramiko.SSHClient()
# 这行代码的作用是允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# connect方法，分别输入ip、端口、账户、密码（或秘钥文件）
ssh.connect('10.10.100.75', 22, 'root', 'cljslrl0620')
# 通过stdin,stdout,stderr获得exec_command（）执行命令后的返回结果
# 命令执行出错并不会抛出异常，所以，对于命令出错需要根据自己的需求进行相应的处理
stdin, stdout, stderr = ssh.exec_command('ls /')
# stdout  [u'bin\n', u'boot\n', u'CmdTool.log\n', u'dev\n', u'etc\n', u'get_log.log\n', u'home\n', u'lib\n',
# u'lib64\n', u'media\n', u'megacli_data.txt\n', u'MegaSAS.log\n', u'mnt\n', u'opt\n', u'oswbb\n', u'proc\n',
# u'qdata.log\n', u'root\n', u'run\n', u'sbin\n', u'srv\n', u'sys\n', u'tmp\n', u'usr\n', u'var\n']
# stderr []
print stdout.read()
print stderr.read()

stdin, stdout, stderr = ssh.exec_command('cat sad')
# stdout []
# stderr [u'cat: sad: No such file or directory\n']
print stdout.read()
print stderr.read()

# 创建一个sftp对象，可以上传下载文件
# 另一种创建的方法为sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
sftp = ssh.open_sftp()

# get下载文件，需要三个参数，self，目标文件， 下载后的文件位置
sftp.get('/var/log/qdata_test.log', './a.log')
# put上传文件，需要三个参数，self，待上传文件，上传后的位置
sftp.put('a.log', '/a.log')

ssh.close()