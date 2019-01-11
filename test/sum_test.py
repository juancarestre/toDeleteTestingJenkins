import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from sum import mysum

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(mysum(3,4), 7)

