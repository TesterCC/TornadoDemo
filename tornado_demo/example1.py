#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/13 23:11'

# 麦子学院 Tornado入门教程01

import tornado.httpserver
import tornado.ioloop


def handle_request(request):
    message = "Hello! Tornado"
    request.write("HTTP/1.1 200 OK\r\nContent-Length:%d\r\n\r\n%s" % (len(message), message))
    request.finish()

if __name__ == '__main__':
    # 实例化一个http server对象
    http_server = tornado.httpserver.HTTPServer(handle_request)
    # listen 8888 socket prot
    http_server.listen(7777)         # visit to 127.0.0.1:7777
    # 启动事件循环
    tornado.ioloop.IOLoop.instance().start()