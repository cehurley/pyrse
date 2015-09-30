__author__ = 'churley'

from servers.server import PyrseServer

server = PyrseServer('localhost', 1211)
server.run()

