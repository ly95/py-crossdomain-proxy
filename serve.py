#!/usr/bin/env python
# coding: utf-8

import tornado.ioloop
import tornado.web
import requests
import json


__author__ = 'linyang95#aol.com'
__version__ = '0.1.0'


def net_post(uri, payload):
    return requests.post(uri, data=payload)


class MainHandler(tornado.web.RequestHandler):

    def prepare(self):
        self.add_header('Access-Control-Allow-Origin', '*')
        self.add_header('Access-Control-Allow-Methods', 'OPTIONS,GET,POST')
        self.add_header('Access-Control-Allow-Headers', 'Content-Type')

    def post(self):
        self.get()

    def get(self):
        payload = dict((k, self.get_argument(k, ""))
                       for k in self.request.arguments)

        r = net_post(self.get_argument("src", ""), payload)
        self.write(r.text)


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8200)
    tornado.ioloop.IOLoop.current().start()
