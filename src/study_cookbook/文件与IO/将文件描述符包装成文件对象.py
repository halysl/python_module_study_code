# -*- coding: utf-8 -*-
# 文件描述符是一种操作系统层次的概念，处于底层
# 将一个对应于操作系统上一个已打开的I/O通道(比如文件、管道、套接字等)的整型文件描述符，转为文件对象

import os
from socket import socket, AF_INET, SOCK_STREAM


def example_fd_2_file():
    fd = os.open("somefile.txt", os.O_WRONLY | os.O_CREAT)

    f = open(fd, "wt")
    f.write("hello world\n")
    f.close()
    fd.close()


def echo_client(client_sock, addr):
    print('Got connection from', addr)

    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                     closefd=False)

    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                      closefd=False)

    # Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()

    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)
