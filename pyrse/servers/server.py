__author__ = 'churley'

from SocketServer import *
from config.settings import settings
from storage.StorageController import StorageController
import server_utils
import sys
if sys.hexversion >= 0x02070000:
    import importlib
    COMPAT = 'safe'
else:
    COMPAT = 'fallback'

class PyrseServer(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.engines = settings.ENGINES
        self.storage = StorageController(self)
        r_module  = self.engines['memory']['class'][0]
        r_class   = self.engines['memory']['class'][1]

        if COMPAT == 'safe':
            lib = importlib.import_module(r_module)
            storage_class = getattr(lib,  r_class)
        else:
            _temp = __import__(r_module, globals(),
                               locals(), [r_class],-1)
            storage_class = getattr(_temp, r_class)

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


        