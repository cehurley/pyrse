import sys
from StorageEngines import *


class FileStore(PimpyStorageEngine):
    RAMDUMP = 'saveAllFromRam'
    INITFROMDISK = 'initFromFileSystem'
    
    def __init__(self, path):
        self.file = path

    def saveAllFromRam(self, data=None):
        with open(self.file, 'wb') as f:
            for d in data:
                j = str(d[1]).replace('\n', '')
                f.write(d[0] + '|' + d[1] + '\n')


    def initFromFileSystem(self):
        temp = {}
        with open(self.file, 'rb') as f:
            for d in f:
                t = d.split('|')
                temp[t[0]] = t[1].strip()
        return temp


