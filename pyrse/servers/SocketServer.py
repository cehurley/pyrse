__author__ = 'churley'



import asyncore
import socket

class CmdHandler(asyncore.dispatcher_with_send):
    ''' Main handler for socket calls '''
    def __init__(self, sock, app):
        asyncore.dispatcher_with_send.__init__(self, sock)
        self.app = app

    def handle_read(self):
        ''' entry point for interfacing with pyrse '''
        data = self.recv(8192)
        if data:
            # todo: add sanitization here
            r = self.app.cmd(data)
            # todo: hook error codes here
            self.send(r)

class SocketServer(asyncore.dispatcher):

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
            print 'connection from %s' % repr(addr)
            handler = CmdHandler(sock, self.app)

