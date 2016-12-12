from Position import Position
from Grid import Grid
from Ship import Ship
import unittest
import Util

class UtilTestCase(unittest.TestCase):
    
    def test_shipFits(self):
        board = Grid(10, 10) 
        self.assertTrue(Util.shipFits(board, [], 1, Position(0, 0), Ship.ORIENTATION_0_DEG))
        self.assertTrue(Util.shipFits(board, [], 1, Position(0, 0), Ship.ORIENTATION_90_DEG))
        self.assertTrue(Util.shipFits(board, [], 1, Position(0, 0), Ship.ORIENTATION_180_DEG))
        self.assertTrue(Util.shipFits(board, [], 1, Position(0, 0), Ship.ORIENTATION_270_DEG))
        self.assertTrue(Util.shipFits(board, [], 3, Position(0, 0), Ship.ORIENTATION_90_DEG))
        self.assertTrue(Util.shipFits(board, [], 3, Position(8, 8), Ship.ORIENTATION_180_DEG))
        self.assertTrue(Util.shipFits(board, [], 5, Position(5, 5), Ship.ORIENTATION_270_DEG))
        self.assertFalse(Util.shipFits(board, [], 2, Position(0, 0), Ship.ORIENTATION_180_DEG))
        self.assertFalse(Util.shipFits(board, [], 11, Position(0, 0), Ship.ORIENTATION_0_DEG))
        self.assertFalse(Util.shipFits(board, [], 1, Position(10, 10), Ship.ORIENTATION_0_DEG))
        self.assertFalse(Util.shipFits(board, [], 1, Position(9, 10), Ship.ORIENTATION_0_DEG))
        self.assertFalse(Util.shipFits(board, [], 3, Position(9, 9), Ship.ORIENTATION_90_DEG))

    def test_shipFitsOtherShips(self):
        board = Grid(10, 10) 
        placedShips = [Ship('carrier', [1, 1, 1, 1, 1], value=1, boardPosition=Position(1, 1), orientation=Ship.ORIENTATION_0_DEG), Ship('cruiser', [1, 1, 1], value=1, boardPosition=Position(5, 5), orientation=Ship.ORIENTATION_90_DEG)]
        self.assertTrue(Util.shipFits(board, placedShips, 1, Position(0, 0), Ship.ORIENTATION_0_DEG))
        self.assertTrue(Util.shipFits(board, placedShips, 5, Position(0, 0), Ship.ORIENTATION_0_DEG))
        self.assertTrue(Util.shipFits(board, placedShips, 5, Position(2, 2), Ship.ORIENTATION_0_DEG))
        self.assertTrue(Util.shipFits(board, placedShips, 5, Position(0, 0), Ship.ORIENTATION_90_DEG))
        self.assertTrue(Util.shipFits(board, placedShips, 5, Position(6, 1), Ship.ORIENTATION_90_DEG))
        self.assertFalse(Util.shipFits(board, placedShips, 1, Position(2, 1), Ship.ORIENTATION_0_DEG))
        self.assertFalse(Util.shipFits(board, placedShips, 3, Position(4, 5), Ship.ORIENTATION_0_DEG))
        self.assertFalse(Util.shipFits(board, placedShips, 3, Position(5, 5), Ship.ORIENTATION_270_DEG))

    def test_randomPlaceShips(self):
        board = Grid(10, 10) 
        ships = [Ship('a', [1, 1, 1], value=1), Ship('b', [1, 1, 1, 1, 1], value=1), Ship('c', [1], value=1),Ship('d', [1, 1, 1, 1, 1, 1, 1], value=1)]
        Util.randomPlaceShips(board, ships)
        for ship in ships:
            newShipList = [s for s in ships if s.getName() is not ship.getName()]
            self.assertTrue(Util.shipFits(board, newShipList, ship.getLength(), ship.getPosition(), ship.getOrientation()))

    def test_percentageUnhitShipsFit(self):
        shipsA = [Ship('a', [1, 1], value=1)]
        self.assertEquals(1, Util.percentageUnhitShipsFit(shipsA, 2, 2, 2, 2))
        self.assertEquals(1, Util.percentageUnhitShipsFit(shipsA, 10, 10, 5, 5))
        self.assertEquals(0.5, Util.percentageUnhitShipsFit(shipsA, 1, 1, 2, 2))
        self.assertEquals(0.5, Util.percentageUnhitShipsFit(shipsA, 2, 2, 1, 1))
        self.assertEquals(0.25, Util.percentageUnhitShipsFit(shipsA, 1, 2, 1, 1))
        self.assertEquals(0.25, Util.percentageUnhitShipsFit(shipsA, 2, 1, 1, 1))
        self.assertEquals(0.25, Util.percentageUnhitShipsFit(shipsA, 1, 1, 2, 1))
        self.assertEquals(0.25, Util.percentageUnhitShipsFit(shipsA, 1, 1, 1, 2))
        self.assertEquals(0, Util.percentageUnhitShipsFit(shipsA, 1, 1, 1, 1))
        shipsB = [Ship('a', [1, 1], value=1), Ship('b', [0, 1], value=1)]
        self.assertEquals(1, Util.percentageUnhitShipsFit(shipsA, 2, 2, 2, 2))
        self.assertEquals(1, Util.percentageUnhitShipsFit(shipsA, 10, 10, 5, 5))
        self.assertEquals(0.5, Util.percentageUnhitShipsFit(shipsA, 1, 1, 2, 2))
        self.assertEquals(0.5, Util.percentageUnhitShipsFit(shipsA, 2, 2, 1, 1))
        self.assertEquals(0.25, Util.percentageUnhitShipsFit(shipsA, 1, 2, 1, 1))
        self.assertEquals(0.25, Util.percentageUnhitShipsFit(shipsA, 2, 1, 1, 1))
        self.assertEquals(0.25, Util.percentageUnhitShipsFit(shipsA, 1, 1, 2, 1))
        self.assertEquals(0.25, Util.percentageUnhitShipsFit(shipsA, 1, 1, 1, 2))
        self.assertEquals(0, Util.percentageUnhitShipsFit(shipsA, 1, 1, 1, 1))
        shipsC = [Ship('a', [1, 0], value=1), Ship('b', [0, 1], value=1)]
        self.assertEquals(1, Util.percentageUnhitShipsFit(shipsC, 2, 2, 2, 2))

