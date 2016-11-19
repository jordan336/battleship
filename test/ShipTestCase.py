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

    def test_getPositions(self):
        ship = Ship("carrier", [1, 1], 1)
        self.assertTrue(Position(0, 0) in ship.getPositions())
        self.assertTrue(Position(1, 0) in ship.getPositions())
        self.assertFalse(Position(-1, 0) in ship.getPositions())
        self.assertFalse(Position(0, 1) in ship.getPositions())

        ship.place(Position(0, 0), Ship.ORIENTATION_90_DEG)
        self.assertTrue(Position(0, 0) in ship.getPositions())
        self.assertTrue(Position(0, 1) in ship.getPositions())
        self.assertFalse(Position(-1, 0) in ship.getPositions())
        self.assertFalse(Position(1, 0) in ship.getPositions())

        ship.place(Position(0, 0), Ship.ORIENTATION_180_DEG)
        self.assertTrue(Position(0, 0) in ship.getPositions())
        self.assertTrue(Position(-1, 0) in ship.getPositions())
        self.assertFalse(Position(1, 0) in ship.getPositions())
        self.assertFalse(Position(0, 1) in ship.getPositions())

        ship.place(Position(0, 0), Ship.ORIENTATION_270_DEG)
        self.assertTrue(Position(0, 0) in ship.getPositions())
        self.assertTrue(Position(0, -1) in ship.getPositions())
        self.assertFalse(Position(1, 0) in ship.getPositions())
        self.assertFalse(Position(0, 1) in ship.getPositions())

    def test_takeDamage(self):
        ship = Ship("carrier", [1, 3, 2], 1)
        ship.takeDamage(0, 1)
        self.assertEqual(0, ship.damageList[0])
        self.assertEqual(3, ship.damageList[1])
        self.assertEqual(2, ship.damageList[2])
        ship.takeDamage(1, 1)
        self.assertEqual(0, ship.damageList[0])
        self.assertEqual(2, ship.damageList[1])
        self.assertEqual(2, ship.damageList[2])
        ship.takeDamage(2, 2)
        self.assertEqual(0, ship.damageList[0])
        self.assertEqual(2, ship.damageList[1])
        self.assertEqual(0, ship.damageList[2])

    def test_takeDamagePosition(self):
        ship = Ship("carrier", [1, 3, 2], 1)
        ship.takeDamage_Position(Position(0, 0), 1)
        self.assertEqual(0, ship.damageList[0])
        self.assertEqual(3, ship.damageList[1])
        self.assertEqual(2, ship.damageList[2])
        ship.takeDamage_Position(Position(2, 0), 5)
        self.assertEqual(0, ship.damageList[0])
        self.assertEqual(3, ship.damageList[1])
        self.assertEqual(0, ship.damageList[2])
        ship.takeDamage_Position(Position(10, 10), 1)
        self.assertEqual(0, ship.damageList[0])
        self.assertEqual(3, ship.damageList[1])
        self.assertEqual(0, ship.damageList[2])

    def test_getDamage(self):
        ship = Ship("carrier", [1, 3, 2], 1)
        self.assertEqual(6, ship.getDamage())
        ship.takeDamage(0, 1)
        self.assertEqual(5, ship.getDamage())
        ship.takeDamage(0, 1)
        self.assertEqual(5, ship.getDamage())
        ship.takeDamage(1, 5)
        self.assertEqual(2, ship.getDamage())

