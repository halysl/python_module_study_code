import paramiko

ip = ""
port = 22
user = "root"
passwd = "cljslrl0620"
cmd = ""

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(ip, port, user, passwd)
stdin, stdout, stderr = ssh.exec_command(cmd)
