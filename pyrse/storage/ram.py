__author__ = 'churley'

import sys
import time
from StorageEngines import *

class MemoryStore(PimpyStorageEngine):

    def __init__(self):
        self.bag = {}
        self.dump_method = None
        self.init_method = None

    def foot_print(self):
        return sys.getsizeof(self.bag)

    def insert(self, key, val):
        self.bag[key] = str(val)

    def get(self, key):
        try:
            return self.bag[key]
        except:
            return None

    def syncToDisk(self):
        self.dump_method(self.getAll())
        print 'sync to disk completed (',time.time(), ') ', len(self.bag), ' keys'

    def initFromDisk(self):
        print len(self.bag), '=>',
        self.bag = self.init_method()
        print len(self.bag)

    def hasKey(self, key):
        if key in self.bag.keys():
            return True
        else:
            return False

    def delete(self, key):
        try:
            del self.bag[key]
            return True
        except:
            return False

    def getAll(self):
        temp = []
        for k in self.bag.keys():
            temp.append([k,self.bag[k]])
        return temp




