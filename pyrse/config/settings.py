import sys

class settings(object):
    HOMEDIR = sys.path[0]
    DEBUG = 1
    # set up your data stores here
    ENGINES = {'memory':
                   {'engine':'ram', 'class':['storage.ram','MemoryStore']},
               'persistant':
                   {'engine':'file',
                    'class' :['storage.file','FileStore'],
                    'path'  :HOMEDIR+'/data.pimpy'
                   }
              }

