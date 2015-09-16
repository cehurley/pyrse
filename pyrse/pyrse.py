__author__ = 'churley'

from servers.server import PyrseServer

server = PyrseServer('localhost', 8080)
server.run()

