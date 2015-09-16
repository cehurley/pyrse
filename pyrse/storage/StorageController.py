__author__ = 'churley'


class StorageController(object):

    def __init__(self, app):
        self.ram_store = None
        self.persistent_store = None

    def store(self, key, val):
        pass

    def getOne(self, key):
        pass

    def getMany(self, query):
        pass

    def getAll(self):
        pass

    def debugReport(self):
        msg = 'storage controller loaded\n'
        msg += str(self.ram_store)
        return msg


