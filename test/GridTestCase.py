import unittest
import collections
from Grid import Grid
from Position import Position

class GridTestCase(unittest.TestCase):
    
    def test_Create(self):
        grid = Grid(10, 10)
        self.assertEquals(10, grid.getWidth())
        self.assertEquals(10, grid.getHeight())
        self.assertEquals([], grid.getHitPositions())
        self.assertEquals([], grid.getMissedPositions())

    def test_GetValidNeighbors1x1(self):
        grid = Grid(1, 1)
        self.assertEquals([], grid.getValidNeighbors(Position(0, 0)))

    def test_GetValidNeighbors2x2(self):
        grid = Grid(2, 2)
        self.assertEquals(collections.Counter([Position(1,0), Position(0,1)]), collections.Counter(grid.getValidNeighbors(Position(0, 0))))
        self.assertEquals(collections.Counter([Position(0,0), Position(1,1)]), collections.Counter(grid.getValidNeighbors(Position(0, 1))))
        self.assertEquals(collections.Counter([Position(0,0), Position(1,1)]), collections.Counter(grid.getValidNeighbors(Position(1, 0))))
        self.assertEquals(collections.Counter([Position(1,0), Position(0,1)]), collections.Counter(grid.getValidNeighbors(Position(1, 1))))

    def test_GetValidNeighborsAll(self):
        grid = Grid(3, 3)
        expected = collections.Counter([Position(1,0), Position(0,1), Position(1,2), Position(2,1)])
        actual = collections.Counter(grid.getValidNeighbors(Position(1, 1)))
        self.assertTrue(expected == actual)


    def test_HitMissPosition(self):
        grid = Grid(10, 10)
        grid.setHitPosition(Position(1, 1))
        grid.setHitPosition(Position(2, 2))
        self.assertTrue(grid.queryPositionHit(Position(1, 1)))
        self.assertTrue(grid.queryPositionHit(Position(2, 2)))
        self.assertFalse(grid.queryPositionMissed(Position(1, 1)))
        self.assertFalse(grid.queryPositionMissed(Position(2, 2)))
        self.assertEqual(collections.Counter([Position(1, 1), Position(2,2)]), collections.Counter(grid.getHitPositions()))
        self.assertEqual([], grid.getMissedPositions())
        

