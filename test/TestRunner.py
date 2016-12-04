import unittest
import sys
import os
testDirPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(testDirPath + '/../src/')

from PositionTestCase import PositionTestCase
from GridTestCase import GridTestCase
from ShipTestCase import ShipTestCase
from ClassicTorpedoTestCase import ClassicTorpedoTestCase
from StateTestCase import StateTestCase
from UtilTestCase import UtilTestCase

positionSuite = unittest.TestLoader().loadTestsFromTestCase(PositionTestCase)
gridSuite = unittest.TestLoader().loadTestsFromTestCase(GridTestCase)
shipSuite = unittest.TestLoader().loadTestsFromTestCase(ShipTestCase)
classicTorpedoSuite = unittest.TestLoader().loadTestsFromTestCase(ClassicTorpedoTestCase)
stateSuite = unittest.TestLoader().loadTestsFromTestCase(StateTestCase)
utilSuite = unittest.TestLoader().loadTestsFromTestCase(UtilTestCase)

allTests = unittest.TestSuite([positionSuite, gridSuite, shipSuite, classicTorpedoSuite, stateSuite, utilSuite])

unittest.TextTestRunner(verbosity=2).run(allTests)

