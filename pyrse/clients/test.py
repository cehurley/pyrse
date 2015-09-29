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

    def send(self, command, key, data=''):
        cmd = ' '.join([command, key, data])
        self.sock.sendall(cmd)
        received = self.sock.recv(1024)
        #print "Sent:     %s"%(cmd)
        #print "Received: %s"%(received)
	return received

    def save(self, key, data):
        return self.send(pc.STORE, key, data)

    def load(self, key):
        return self.send(pc.LOAD, key)

    def close(self):
        self.sock.close()


if __name__ == '__main__':
    c = PimpyClient('localhost', 8080)
    print 'saving'
    c.save('01082', "{'name':'bobbycakes'}")
    print 'getting'
    c.load('01082')
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


