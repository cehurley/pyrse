__author__ = 'churley'



import asyncore
import socket

class EchoHandler(asyncore.dispatcher_with_send):

    def __init__(self, sock, app):
        asyncore.dispatcher_with_send.__init__(sock)
        self.app = app


    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.app.cmd(data)
            self.send(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, app):
        asyncore.dispatcher.__init__(self)
        self.app = app
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((app.host, app.port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = EchoHandler(sock, self.app)

