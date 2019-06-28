import paramiko
from contextlib import contextmanager


@contextmanager
def get_ssh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('10.10.100.6', 22, 'root', 'cljslrl0620')
    yield ssh

# with get_ssh() as ssh:
#     i,o,e = ssh.exec_command('ls')
#     print o.read()


def a():
    with get_ssh() as ssh:
        i, o, e = ssh.exec_command('ls')
        return ssh


def b(ssh):
    i, o, e = ssh.exec_command('hostname')
    print o.read()

if __name__ == "__main__":
    ssh = a()
    b(ssh)
    ssh.close()
