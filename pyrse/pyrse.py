__author__ = 'churley'

from servers.server import PimpyServer

server = PimpyServer('localhost', 8080)
server.run()

