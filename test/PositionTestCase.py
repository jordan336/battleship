import unittest
from Position import Position

class PositionTestCase(unittest.TestCase):

    def test_Create(self):
        pos = Position(1, 2)
        self.assertEqual(1, pos.x)
        self.assertEqual(2, pos.y)

    def test_GetPosition(self):
        pos = Position(0, -2)
        self.assertEquals((0, -2), pos.getPosition())

    def test_Equals(self):
        pos1 = Position(-1, 2)
        pos2 = Position(-1, 2)
        self.assertTrue(pos1 == pos2)

    def test_NotEquals(self):
        pos1 = Position(-1, -2)
        pos2 = Position(-1, 0)
        self.assertFalse(pos1 == pos2)

    def test_EqualsInvalidType(self):
        pos1 = Position(0, 0)
        other = (0, 0)
        self.assertFalse(pos1 == other)
        

