__author__ = 'churley'
import unittest
import subprocess
import sys
import uuid
sys.path.append('/Users/churley/pyrse/pyrse')
sys.path.append('/Users/chadhurley/pyrse/pyrse')
from servers.server import PyrseServer
from clients.test import PimpyClient


class ServerTestCase(unittest.TestCase):
    def setUp(self):
        #self.server = PyrseServer('localhost', 8080)
        #proc = subprocess.Popen('cd ..;python pyrse.py', shell=True)
        self.c = PimpyClient('localhost', 1211)
    def tearDown(self):
        #proc = subprocess.Popen('pkill pyrse.py', shell=True)
        self.c.close()
        #print 'closing socket connection', self.c
    def testSend(self):
        """ testing a send/save """
        temp = self.c.save('01082', "{'name':'bobbycakes'}")
        assert temp.strip()  == '01082', 'not pass'

    def testReceive(self):
        temp = self.c.load('01082')
        assert temp.strip() == "{'name':'bobbycakes'}", "bad get"

    def testSave10000(self):
        for i in xrange(10500):
            u = uuid.uuid4()
            temp = self.c.save(str(u), "{'name': '%s'}"%str(u))
            assert temp.strip() == str(u), "bad save"

    def testLoad10000(self):
        for i in xrange(10500):
            temp = self.c.load(str(i))
            assert temp.strip() == "{'name': 'object%d'}"%i, "bad load"

if __name__ == "__main__":
    unittest.main()
