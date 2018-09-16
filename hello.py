#!/usr/bin/env python
#  -*-coding:utf-8-*-

import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        self.write("hello world")

    def post(self, *args, **kwargs):
        self.write("hello world")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    # app.listen(8000)
    http_server = tornado.httpserver.HTTPServer(app)
    # http_server.listen(8000)
    # 开启多进程
    http_server.bind(8000)
    http_server.start(0)
    tornado.ioloop.IOLoop.current().start()
