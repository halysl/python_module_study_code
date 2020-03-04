#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: run.py
# Desc:
# Author: light
# Email: zhi.liu@woqutech.com
# HomePage: www.woqutech.com
# Version: 0.1.0
# LastChange: 2019/10/21 上午09:46
# History:
#=============================================================================
"""

import os
import json
import logging
import dateutil.parser
from datetime import timedelta, datetime

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.web import RequestHandler
from tornado.options import options, define
from tornado.web import URLSpec as U

import requests

define("port", default=23123, help="run on the given port", type=int)
define("debug", default=False, help="start debug mode", type=bool)

logger = logging.getLogger(logging.basicConfig(filename='/var/log/build_webhook.log',level=logging.INFO,format='%(levelname)s:%(asctime)s:%(message)s'))

class GetStatusHandler(RequestHandler):
    def render_info(self, msg):
        key = "cbd6176e-9f0b-4a78-b8b2-ad8a8252e329"
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key="
        push_url = "".join((base_url, key))
        logger.info("push_url:{}".format(push_url))

        send_msg = ("项目名<font color=\"info\">{}</font>\n"
           ">开始时间<font color=\"info\">{}</font>\n"
           ">结束时间<font color=\"info\">{}</font>\n"
           ">执行结果<font color=\"info\">{}</font>\n"
           ">错误信息<font color=\"info\">{}</font>\n").format(msg["project_name"], msg["start_time"], msg["finish_time"], msg["status"], msg["traceback"])
        data = {
        "msgtype": "markdown",
        "markdown": {
            "content": send_msg,
            "mentioned_list": [],
            "mentioned_mobile_list": []
            }
        }
        logger.info("notification msg:{}".format(data))
        r = requests.post(push_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

    def parse_data(self, data_dict):
        send = False
        msg = {}
        do_what = data_dict.get("friendly_name", "unknown msg")
        if do_what == u"Project Update":
            pass
        elif do_what == u"Job":
            msg["project_name"] = data_dict["project"]
            msg["status"] = data_dict["status"]
            msg["start_time"] = datetime.strftime(dateutil.parser.parse(data_dict["started"]) + timedelta(hours=16), '%Y年%m月%d日 %H:%M:%S')
            msg["finish_time"] = datetime.strftime(dateutil.parser.parse(data_dict["finished"]) + timedelta(hours=16), '%Y年%m月%d日 %H:%M:%S')
            msg["traceback"] = ""
            if msg["status"] != "successful":
                msg["traceback"] = data_dict["traceback"]
            send = True
        else:
            pass
        return send, msg

    def post(self):
        # {u'status': u'successful', u'name': u'zhongguoyidong-6.3.0', u'started': u'2019-10-20T18:44:23.692415+00:00', u'traceback': u'', u'friendly_name': u'Project Update', u'created_by': u'None', u'url': u'https://192.168.1.99/#/scm_update/1851', u'finished': u'2019-10-20T18:44:33.629823+00:00', u'id': 1851}
        data = json.loads(self.request.body, strict=False)
        logger.info(data)
        send, msg = self.parse_data(data)
        if send:
            self.render_info(msg)
        return self.write("bbb")

urls = [
    U('/v1/call', GetStatusHandler),
]


class Application(tornado.web.Application):
    def __init__(self):
        app_settings = dict(
            debug=options.debug,
        )
        super(Application, self).__init__(urls, **app_settings)


def main():
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    logger.info("Server start on port %s", options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
