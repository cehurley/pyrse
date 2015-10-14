__author__ = 'churley'

from SocketServer import *
from config.settings import settings
from storage.StorageController import StorageController
import server_utils
import sys
from config.environment import Environment
import time
from threading import Thread

env = Environment(debug=True)
if env.compat == Environment.SAFE:
    import importlib


class PyrseServer(object):
    ''' Main server class. This is the main app controller '''
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.engines = settings.ENGINES
        self.storage = StorageController(self)
        # see conig/setting.py for format of these.
        # allows override of the in-memory store
        
        print 'Initializing Ram Storage'
        r_module  = self.engines['memory']['class'][0]
        r_class   = self.engines['memory']['class'][1]

        if env.compat == Environment.SAFE:
            lib = importlib.import_module(r_module)
            storage_class = getattr(lib,  r_class)
        else:
            _temp = __import__(r_module, globals(),
                               locals(), [r_class],-1)
            storage_class = getattr(_temp, r_class)

        self.storage.ram_store = storage_class()
        if settings.DEBUG == 1:
            print self.storage.debugReport()

        print 'Checking for persistant Storage: ',
        if self.engines.has_key('persistant'):
            print 'found'
            p_module  = self.engines['persistant']['class'][0]
            p_class   = self.engines['persistant']['class'][1]
            p_path    = self.engines['persistant']['path']

            if env.compat == Environment.SAFE:
                lib = importlib.import_module(p_module)
                p_storage_class = getattr(lib,  p_class)
            else:
                _ptemp = __import__(p_module, globals(),
                               locals(), [p_class],-1)
                p_storage_class = getattr(_ptemp, p_class)
            self.storage.persistant_store = p_storage_class(p_path)

            if hasattr(p_storage_class, 'RAMDUMP'):
                dump_method = getattr(self.storage.persistant_store, 
                                        p_storage_class.RAMDUMP)
                self.storage.ram_store.dump_method = dump_method

            if hasattr(p_storage_class, 'INITFROMDISK'):
                init_method = getattr(self.storage.persistant_store, 
                                        p_storage_class.INITFROMDISK)
                self.storage.ram_store.init_method = init_method
                
            self.storage.ram_store.initFromDisk()



    def run(self):
        print 'starting Pyrse. . .'
        server = SocketServer(self)
        print "listening on %s:%s"%(self.host, self.port)
        print 'starting background syncer'
        t = Thread(target=self.backgroundSync)
        t.setDaemon(True)
        t.start()
        print 'done'
        asyncore.loop()

    def cmd(self, msg):
        ''' main entry for parsing commands '''
        c,k,d = server_utils.parseCommand(msg)
        func = getattr(self, c)
        return func(k,d)

    def store(self, key, data):
        # todo: add switch for ram vs disk
        return self.storage.store(key, data)

    def loadone(self, key, data=''):
        return self.storage.getOne(key)

    def backgroundSync(self):
        while 1 == 1:
            self.storage.ram_store.syncToDisk()
            time.sleep(30)
        
