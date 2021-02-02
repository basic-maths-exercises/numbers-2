try:
    from AssCheck import funcchecks as fc
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AssCheck"])
    from AssCheck import funcchecks as fc

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self):
        inputs, outputs = [], []
        for i in range(20) :
            val = np.random.randint(1,9999)
            inputs.append((val,))
            nthou = np.floor( val / 1000)
            outputs.append( np.floor( (val - nthou*1000) / 100 ) ) 
        assert( fc.check_func('numberOfHundreds', inputs, outputs ) )
