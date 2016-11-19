import unittest
from ClassicTorpedo import ClassicTorpedo
from Position import Position

class ClassicTorpedoTestCase(unittest.TestCase):

    def test_Create(self):
        torpedo = ClassicTorpedo()
        self.assertEqual(torpedo.getTorpedoType(), ClassicTorpedo.TORPEDO_TYPE_CLASSIC)

    def test_GetDamage(self):
        torpedo = ClassicTorpedo()
        self.assertEqual(1, torpedo.getDamage(Position(0, 0), Position(0, 0)))
        self.assertEqual(0, torpedo.getDamage(Position(0, 0), Position(1, 1)))
        self.assertEqual(0, torpedo.getDamage(Position(0, 0), Position(0, 1)))
        self.assertEqual(0, torpedo.getDamage(Position(0, 0), Position(1, 0)))
        self.assertEqual(0, torpedo.getDamage(Position(1, 1), Position(0, 0)))
        self.assertEqual(1, torpedo.getDamage(Position(1, 1), Position(1, 1)))
        self.assertEqual(0, torpedo.getDamage(Position(1, 1), Position(0, 1)))
        self.assertEqual(0, torpedo.getDamage(Position(1, 1), Position(1, 0)))

