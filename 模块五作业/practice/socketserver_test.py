#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__='Eric'
#Date:2018/4/8


import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        pass


s = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyServer)
s.serve_forever()