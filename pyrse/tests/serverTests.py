__author__ = 'churley'
import unittest
import subprocess
import sys
sys.path.append('/Users/churley/pyrse/pyrse')
from servers.server import PyrseServer
from clients.test import PimpyClient


class ServerTestCase(unittest.TestCase):
    def setUp(self):
        #self.server = PyrseServer('localhost', 8080)
        #proc = subprocess.Popen('cd ..;python pyrse.py', shell=True)
	pass
    def tearDown(self):
        #proc = subprocess.Popen('pkill pyrse.py', shell=True)
	pass
    def testSend(self):
	""" testing a send/save """
        c = PimpyClient('localhost', 8080)
	temp = c.save('01082', "{'name':'bobbycakes'}")
        assert temp.strip()  == '01082', 'not pass'

    def testReceive(self):
        assert 1 == 1

if __name__ == "__main__":
    unittest.main()
