# -*- coding:utf-8 -*-
import time
from tornado import gen
from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future


def synchronous_fetch(url):
    """
    常规网络请求（同步）
    :param url:
    :return:
    """
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


def asynchronous_fetch(url, callback):
    """
    有回调函数的网络请求（异步）
    :param url:
    :param callback:
    :return:
    """
    http_client = AsyncHTTPClient()
    def handler_response(response):
        callback(response.body)
    http_client.fetch(url)


def async_fetch_future(url):
    """
    使用future对象的网络请求（异步）
    :param url:
    :return:
    """
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    fetch_future.add_done_callback(
        lambda f: my_future.set_result(f.result())
    )
    return my_future


@gen.coroutine
def fetch_coroutine(url):
    """
    使用装饰器的网络请求（异步）
    :param url:
    :return:
    """
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise gen.Return(response.body)


def time_count(func):
    def wrapper():
        timestart = time.time()
        print(timestart)
        func()
        timeend = time.time()
        print(timeend)
        timecounts = (timeend - timestart)
        print('func costs time %s'%timecounts)
    return wrapper
