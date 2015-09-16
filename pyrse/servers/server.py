__author__ = 'churley'


from SocketServer import *
from config.settings import settings
from storage.StorageController import StorageController
import server_utils
import importlib

class PyrseServer(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.engines = settings.ENGINES
        self.storage = StorageController(self)
        lib = importlib.import_module(self.engines['memory']['class'][0])
        storage_class = getattr(lib,  self.engines['memory']['class'][1])
        self.storage.ram_store = storage_class()
        if settings.DEBUG == 1:
            print self.storage.debugReport()

    def run(self):
        print 'starting tcp server'
        server = SocketServer(self)
        print 'started!!!!'
        asyncore.loop()

    def cmd(self, msg):
        c,k,d = server_utils.parseCommand(msg)
        func = getattr(self, c)
        return func(k,d)

    def store(self, key, data):
        return self.storage.store(key, data)

    def loadone(self, key, data=''):
        return self.storage.getOne(key)


        