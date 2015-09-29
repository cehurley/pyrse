__author__ = 'churley'


class StorageController(object):

    def __init__(self, app):
        self.ram_store = None
        self.persistent_store = None

    def store(self, key, data):
        self.ram_store.insert(key, data)
        #print self.ram_store.foot_print()
        #print self.ram_store.getAll()
        return key

    def getOne(self, key):
        return self.ram_store.get(key)

    def getMany(self, query):
        pass

    def getAll(self):
        pass


    def debugReport(self):
        msg = 'storage controller loaded\n'
        msg += str(self.ram_store)
        return msg


