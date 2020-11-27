import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self):
        for i in range(20) :
            val = np.random.randint(1,9999)
            nthou = int( np.floor( val / 1000) )
            nhund = int( np.floor( (val - nthou*1000) / 100 ) ) 
            self.assertTrue( nhund==numberOfHundreds(val), "Your function is not working correctly" )
