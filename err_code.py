#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义返回http的error，每组20个, 以1000开始

error_message = {}

# auth error
AUTH_ERROR = 403
error_message.update({AUTH_ERROR: u"认证失败"})

INTERNAL_ERROR = 1000
HTTP_QUERY_PARAM = 1001
HTTP_BODY_PARAM = 1002

error_message.update({
    INTERNAL_ERROR: u"程序内部错误",
    HTTP_QUERY_PARAM: u"查询参数错误",
    HTTP_BODY_PARAM: u"参数错误",
})