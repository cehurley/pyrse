__author__ = 'churley'


import socket
import sys
from commands import pc

class PimpyClient(object):

    def __init__(self, host, port):
        self.host, self.port = host, port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Connect to server and send data
            self.sock.connect((self.host, self.port))
        except:
            print "couldn't get a socket"

    def send(self, command, data):
        for i in range(5):
            self.sock.sendall(command+' :'+data + "\n")
            received = self.sock.recv(1024)
            print "Sent:     {}".format(data)
            print "Received: {}".format(received)


    def save(self, data):
        self.send(pc.STORE, data)


    def close(self):
        self.sock.close()


c = PimpyClient('localhost', 8080)
c.save("{'key':'val'}")
c.close()



'''
p = pimpy_client()
p.use('users')
p.stats('records')
obj = p.load(key)
obj.name = 'blah blah'
obj.save()
p.close()
p.export('xml')
p.export('csv')
p.export('html')
p.export('parsable')
p.export('dump')
p.import(filename)
'''


