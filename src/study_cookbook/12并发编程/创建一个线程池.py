# -*- coding: utf-8 -*-
import threading
import random
from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor

"""
下面的多线程 通过 python3 的 concurrent 模块实现，但python2是没有这个模块的

# def echo_client(sock, client_addr):
#     '''
#     Handle a client connection
#     '''
#     print('Got connection from', client_addr)
#     while True:
#         msg = sock.recv(65536)
#         if not msg:
#             break
#         sock.sendall(msg)
#     print('Client closed connection')
#     sock.close()


# def echo_server(addr):
#     pool = ThreadPoolExecutor(128)
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.bind(addr)
#     sock.listen(5)
#     while True:
#         client_sock, client_addr = sock.accept()
#         pool.submit(echo_client, client_sock, client_addr)


# echo_server(('', 15000))
"""

"""
下面是 python2 的实现
"""


def func(a):
    return a


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        print("Starting " + threading.currentThread().name)
        self.result = self.func(*self.args)
        print("Exiting " + threading.currentThread().name)

    def get_result(self):
        threading.Thread.join(self)  # 等待线程执行完毕
        try:
            return self.result
        except Exception:
            return None

if __name__ == "__main__":
    rets = []
    li = []
    for i in range(4):
        li.append(MyThread(func, (random.randint(1, 100),)))

    for l in li:
        l.start()

    for l in li:
        l.join()

    for l in li:
        rets.append(l.get_result())
    print(rets)
