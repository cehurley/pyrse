__author__ = 'churley'

import sys
from StorageEngines import *

class MemoryStore(PimpyStorageEngine):

    def __init__(self):
        self.bag = {}

    def foot_print(self):
        return sys.getsizeof(self.bag)

    def insert(self, key, val):
        self.bag[key] = val

    def get(self, key):
        try:
            return self.bag[key]
        except:
            return None

    def delete(self, key):
        try:
            del self.bag[key]
            return True
        except:
            return False

    def getAll(self):
        temp = []
        for k,v in self.bag:
            temp.append([k,v])
        return temp




