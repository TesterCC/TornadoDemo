#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

#定义具体由那一个RequestHandler来处理请求
class Application(tornado.web.Application):
    def __init__(self):

        # URL映射
        handlers = [(r'/', HomeHandler),
                    (r'/login', LoginHandler)]
        settings = dict(template_path=os.path.join(os.path.dirname(__file__), 'templates'),
                        static_path=os.path.join(os.path.dirname(__file__), 'static'),
                        blog_title="Tornado Blog"
                        )

        super(Application, self).__init__(handlers, **settings)

#为请求生成响应的内容
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('/login')

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html', error='')

def main():
    port = 8888
    #监听socket套接字，读取http请求,调用对应的handler,并且用HTTPServer.write返回数据给客户端
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
