import unittest
from Ship import Ship
from Position import Position

class ShipTestCase(unittest.TestCase):

    def test_Create(self):
        ship = Ship("carrier", [1, 2, 1], 1, Position(1, 1), Ship.ORIENTATION_180_DEG) 
        self.assertEqual("carrier", ship.getName())
        self.assertEqual(Position(1, 1), ship.getPosition())
        self.assertEqual(3, ship.getLength())
        self.assertEqual(Ship.ORIENTATION_180_DEG, ship.getOrientation())

        ship2 = Ship("destroyer", [1], 1) 
        self.assertEqual("destroyer", ship2.getName())
        self.assertEqual(Position(0, 0), ship2.getPosition())
        self.assertEqual(1, ship2.getLength())
        self.assertEqual(Ship.ORIENTATION_0_DEG, ship2.getOrientation())

    def test_hasShip(self):
        ship = Ship("carrier", [1, 1], 1)
        self.assertTrue(ship.hasShip(Position(0, 0)))
        self.assertTrue(ship.hasShip(Position(1, 0)))
        self.assertFalse(ship.hasShip(Position(2, 0)))
        self.assertFalse(ship.hasShip(Position(0, -1)))
        self.assertFalse(ship.hasShip(Position(1, 1)))

        ship.place(Position(0, 0), Ship.ORIENTATION_180_DEG)
        self.assertTrue(ship.hasShip(Position(0, 0)))
        self.assertTrue(ship.hasShip(Position(-1, 0)))
        self.assertFalse(ship.hasShip(Position(1, 0)))
        self.assertFalse(ship.hasShip(Position(0, 2)))
        self.assertFalse(ship.hasShip(Position(-2, 0)))
        self.assertFalse(ship.hasShip(Position(0, 1)))

    def test_shipSegmentIndex(self):
        ship = Ship("carrier", [1, 1, 1], 1)
        self.assertEqual(0, ship.shipSegmentIndex(Position(0, 0)))
        self.assertEqual(1, ship.shipSegmentIndex(Position(1, 0)))
        self.assertEqual(2, ship.shipSegmentIndex(Position(2, 0)))
        self.assertEqual(-1, ship.shipSegmentIndex(Position(3, 0)))
        self.assertEqual(-1, ship.shipSegmentIndex(Position(0, -1)))
        self.assertEqual(-1, ship.shipSegmentIndex(Position(-1, 0)))
        self.assertEqual(-1, ship.shipSegmentIndex(Position(1, 1)))

        ship.place(Position(-1, -1), Ship.ORIENTATION_90_DEG)
        self.assertEqual(0, ship.shipSegmentIndex(Position(-1, -1)))
        self.assertEqual(1, ship.shipSegmentIndex(Position(-1, 0)))
        self.assertEqual(2, ship.shipSegmentIndex(Position(-1, 1)))
        self.assertEqual(-1, ship.shipSegmentIndex(Position(-1, 2)))
        self.assertEqual(-1, ship.shipSegmentIndex(Position(0, 0)))
        self.assertEqual(-1, ship.shipSegmentIndex(Position(-1, -2)))

        ship.place(Position(-1, -1), Ship.ORIENTATION_270_DEG)
        self.assertEqual(0, ship.shipSegmentIndex(Position(-1, -1)))
        self.assertEqual(1, ship.shipSegmentIndex(Position(-1, -2)))
        self.assertEqual(2, ship.shipSegmentIndex(Position(-1, -3)))
        self.assertEqual(-1, ship.shipSegmentIndex(Position(-1, -4)))
        self.assertEqual(-1, ship.shipSegmentIndex(Position(-1, 0)))
        self.assertEqual(-1, ship.shipSegmentIndex(Position(0, 0)))
        self.assertEqual(-1, ship.shipSegmentIndex(Position(-2, -1)))


