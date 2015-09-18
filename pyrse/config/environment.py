__author__ = 'churley'

import sys
import os


class Environment(object):

    SAFE = 'safe - python 2.7 or better'
    FALLBACK = '< python 2.7'

    def __init__(self, debug=False):

        self.py_version = sys.hexversion
        if self.py_version >= 0x02070000:
            self.compat = self.SAFE
        else:
            self.compat = self.FALLBACK

        print "Python Version: %x"%self.py_version, self.compat

        self.platform = os.uname()
        print "OS info: %s %s %s"%(self.platform[0],
                                   self.platform[2],
                                   self.platform[4])
