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

positionSuite = unittest.TestLoader().loadTestsFromTestCase(PositionTestCase)
gridSuite = unittest.TestLoader().loadTestsFromTestCase(GridTestCase)
shipSuite = unittest.TestLoader().loadTestsFromTestCase(ShipTestCase)
classicTorpedoSuite = unittest.TestLoader().loadTestsFromTestCase(ClassicTorpedoTestCase)
stateSuite = unittest.TestLoader().loadTestsFromTestCase(StateTestCase)

allTests = unittest.TestSuite([positionSuite, gridSuite, shipSuite, classicTorpedoSuite, stateSuite])

unittest.TextTestRunner(verbosity=2).run(allTests)

