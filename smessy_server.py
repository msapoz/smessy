#! /usr/bin/env python

from circuits.net.sockets import TCPServer

class PongServer(TCPServer):

    def connect(self, sock, host, port):
        self.write(sock, 'HTTP/1.0 200 OK\r\nContent-Length: 5\r\n\r\nPong!\r\n')
        self.close(sock)

PongServer(('localhost', 8050)).run()
