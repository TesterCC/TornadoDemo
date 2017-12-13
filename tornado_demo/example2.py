#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/14 00:05'


# 麦子学院 Tornado入门教程01

import os

import tornado.httpserver
import tornado.ioloop
import tornado.web


class HomeHandler(tornado.web.RequestHandler):
    """
    Bind with login.html
    """
    def get(self, *args, **kwargs):
        self.render('login.html', error="")


class FormHandler(tornado.web.RequestHandler):

    def post(self):
        raise tornado.web.HTTPError(status_code=416, log_message='testing', reason='Form submit is not supported yet!')


class HelloHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        message = "Hello! Tornado2"
        self.write(message)


class OtherHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect('/')


class CustomErrorHandler(tornado.web.RequestHandler):
    """
    return user custom error
    """
    def get(self, *args, **kwargs):
        raise tornado.web.HTTPError(status_code=416, log_message='testing error', reason='unknown request, please visit 127.0.0.1:7777')


class CustomApplication(tornado.web.Application):   # tornado IO映射必须放在这里面

    def __init__(self):
        # 加入URL映射list
        handles = [
            (r'/', HomeHandler),
            (r'/login', HomeHandler),
            (r'/auth/login', FormHandler),
            (r'/test', HelloHandler),
            # (r'/.*', HomeHandler),
            # (r'/.*', tornado.web.RedirectHandler, {'url': '/'}),   # redirect to /  simple
            # (r'/.*', OtherHandler),   # redirect to /  recommend
            (r'/error', CustomErrorHandler),   # return user custom error
        ]

        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), 'templates'),   # 文件所在目录和templates拼接路径
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),   # 文件所在目录和templates拼接路径
            'blog_title': 'Simple Blog'
        }

        super(CustomApplication, self).__init__(handles, **settings)


if __name__ == '__main__':
    # 实例化一个http server对象
    http_server = tornado.httpserver.HTTPServer(CustomApplication())
    # 监听7777 套接字端口
    http_server.listen(7777)
    tornado.ioloop.IOLoop.instance().start()