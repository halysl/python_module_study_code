# -*- coding: utf-8 -*-
import threading


def print_hello():
    print("current threding name:{}\n"
          "hello!\n".format(threading.current_thread().name))


def create_thread(thread_name, func):
    return threading.Thread(target=func, name=thread_name)


def test():
    t_son = create_thread("thread son", print_hello)
    t_son_son = create_thread("thread son son",
                              create_thread("thread son", print_hello))
    t_son.start()
    t_son.join()

    t_son_son.start()
    t_son_son.join()

if __name__ == "__main__":
    test()
