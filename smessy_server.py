#! /usr/bin/env python

from circuits.net.sockets import TCPServer

class PongServer(TCPServer):

    def read(self, sock, data):
        print "I haz sms:", data

PongServer(('newyr.me', 8050)).run()
