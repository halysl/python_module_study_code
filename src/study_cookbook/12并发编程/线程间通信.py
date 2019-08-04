# -*- coding: utf-8 -*-
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c12/p03_communicating_between_threads.html
# 通过 Queue 来进行线程间通信
from queue import Queue
from threading import Thread

# Object that signals shutdown
_sentinel = object()


def producer(out_q):
    while running:
        # Produce some data
        out_q.put(data)

    # Put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)


def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()

        # Check for termination
        if data is _sentinel:
            in_q.put(_sentinel)
            break


q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
