import unittest
from State import State
from Grid import Grid
from ClassicTorpedo import ClassicTorpedo
from Ship import Ship
from Position import Position

class StateTestCase(unittest.TestCase):

    def test_Create(self):
        board = Grid(10, 10)
        state = State([board], [[]], [[]], 1)

        self.assertEqual(board, state.getBoards()[0])
        self.assertEqual([[]], state.getShips())
        self.assertEqual([[]], state.getTorpedos())
        self.assertEqual(0, state.currentAgent())

    def test_DeepCopy(self):
        board = Grid(10, 10)
        torpedos = [ClassicTorpedo(), ClassicTorpedo()]
        ships = [Ship("shipA", [1], 1), Ship("shipB", [1, 1], 1, Position(1, 1))]
        state = State([board], [ships], [torpedos], 1)

        copied = state.deepCopy()

        self.assertEquals(state.currentAgent(), copied.currentAgent())
        self.assertEquals(state.numAgents, copied.numAgents)

        # check game board for deep copy
        copied.getBoards()[0].setHitPosition(Position(0, 0))
        copied.getBoards()[0].setMissedPosition(Position(1, 1))
        self.assertTrue(copied.getBoards()[0].queryPositionHit(Position(0, 0)))
        self.assertTrue(copied.getBoards()[0].queryPositionMissed(Position(1, 1)))
        self.assertEqual(1, len(copied.getBoards()[0].getHitPositions()))
        self.assertEqual(1, len(copied.getBoards()[0].getMissedPositions()))
        self.assertFalse(state.getBoards()[0].queryPositionHit(Position(0, 0)))
        self.assertFalse(state.getBoards()[0].queryPositionMissed(Position(1, 1)))
        self.assertEqual(0, len(state.getBoards()[0].getHitPositions()))
        self.assertEqual(0, len(state.getBoards()[0].getMissedPositions()))

        # check ships for deep copy
        copied.getShips()[0][0].place(Position(5, 5), Ship.ORIENTATION_90_DEG)
        copied.getShips()[0][1].place(Position(9, 9), Ship.ORIENTATION_270_DEG)
        self.assertEqual(Position(5, 5), copied.getShips()[0][0].getPosition())
        self.assertEqual(Position(9, 9), copied.getShips()[0][1].getPosition())
        self.assertEqual(Ship.ORIENTATION_90_DEG, copied.getShips()[0][0].getOrientation())
        self.assertEqual(Ship.ORIENTATION_270_DEG, copied.getShips()[0][1].getOrientation())
        self.assertEqual(Position(0, 0), state.getShips()[0][0].getPosition())
        self.assertEqual(Position(1, 1), state.getShips()[0][1].getPosition())
        self.assertEqual(Ship.ORIENTATION_0_DEG, state.getShips()[0][0].getOrientation())
        self.assertEqual(Ship.ORIENTATION_0_DEG, state.getShips()[0][1].getOrientation())

        # check torpedos for deep copy
        self.assertTrue(copied.getTorpedos()[0][0] is not state.getTorpedos()[0][0])
        self.assertTrue(copied.getTorpedos()[0][1] is not state.getTorpedos()[0][1])
        self.assertEqual(len(copied.getTorpedos()[0]), len(state.getTorpedos()[0]))
        
    # TODO: enable when State.py is fixed with list of lists
    """ 
    def test_BadCreate(self):
        # added agents, but no boards, ships, torpedos
        with self.assertRaises(RuntimeError):
            state = State([], [], [], 3)
    
        # ...
    """

