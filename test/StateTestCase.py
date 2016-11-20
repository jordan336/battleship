import unittest
import collections
from State import State
from Grid import Grid
from ClassicTorpedo import ClassicTorpedo
from Ship import Ship
from Position import Position

class StateTestCase(unittest.TestCase):

    def test_Create(self):
        board = Grid(10, 10)
        board2 = Grid(3, 3)
        state = State(["a1", "a2"], {"a1":board, "a2":board2}, {"a1":[],"a2":[]}, {"a1":[],"a2":[]})
        self.assertEqual("a1", state.getAgents()[0])
        self.assertEqual("a2", state.getAgents()[1])
        self.assertEqual(board, state.getBoard()["a1"])
        self.assertEqual(board2, state.getBoard()["a2"])
        self.assertEqual([], state.getShips()["a1"])
        self.assertEqual([], state.getShips()["a2"])
        self.assertEqual([], state.getTorpedos()["a1"])
        self.assertEqual([], state.getTorpedos()["a2"])
        self.assertEqual("a1", state.currentAgent())

    def test_BadCreate(self):
        # One agent
        with self.assertRaises(RuntimeError):
            State(["a1"], {"a1":Grid(1,1)}, {"a1":[]}, {"a1":[]})
        # Missing gameboard
        with self.assertRaises(RuntimeError):
            State(["a1", "a2"], {"a1":Grid(1,1)}, {"a1":[],"a2":[]}, {"a1":[],"a2":[]})
        # Missing ship list
        with self.assertRaises(RuntimeError):
            State(["a1", "a2"], {"a1":Grid(1,1), "a2":Grid(2,2)}, {"a1":[]}, {"a1":[],"a2":[]})
        # Missing torpedo list
        with self.assertRaises(RuntimeError):
            State(["a1", "a2"], {"a1":Grid(1,1), "a2":Grid(1,1)}, {"a1":[], "a2":[]}, {"a2":[]})

    def test_DeepCopy(self):
        board = Grid(10, 10)
        board2 = Grid(10, 10)
        torpedos = [ClassicTorpedo(), ClassicTorpedo()]
        ships = [Ship("shipA", [1], 1), Ship("shipB", [1, 1], 1, Position(1, 1))]
        state = State(["a1", "a2"], {"a1":board, "a2":board2}, {"a1":ships, "a2":ships}, {"a1":torpedos, "a2":torpedos})

        copied = state.deepCopy()

        self.assertEquals(state.currentAgent(), copied.currentAgent())

        # check game board for deep copy
        copied.getBoard("a1").setHitPosition(Position(0, 0))
        copied.getBoard("a1").setMissedPosition(Position(1, 1))
        self.assertTrue(copied.getBoard("a1").queryPositionHit(Position(0, 0)))
        self.assertTrue(copied.getBoard("a1").queryPositionMissed(Position(1, 1)))
        self.assertEqual(1, len(copied.getBoard("a1").getHitPositions()))
        self.assertEqual(1, len(copied.getBoard("a1").getMissedPositions()))
        self.assertFalse(state.getBoard("a1").queryPositionHit(Position(0, 0)))
        self.assertFalse(state.getBoard("a1").queryPositionMissed(Position(1, 1)))
        self.assertEqual(0, len(state.getBoard("a1").getHitPositions()))
        self.assertEqual(0, len(state.getBoard("a1").getMissedPositions()))

        # check ships for deep copy
        copied.getShips("a1")[0].place(Position(5, 5), Ship.ORIENTATION_90_DEG)
        copied.getShips("a1")[1].place(Position(9, 9), Ship.ORIENTATION_270_DEG)
        self.assertEqual(Position(5, 5), copied.getShips("a1")[0].getPosition())
        self.assertEqual(Position(9, 9), copied.getShips("a1")[1].getPosition())
        self.assertEqual(Ship.ORIENTATION_90_DEG, copied.getShips("a1")[0].getOrientation())
        self.assertEqual(Ship.ORIENTATION_270_DEG, copied.getShips("a1")[1].getOrientation())
        self.assertEqual(Position(0, 0), state.getShips("a1")[0].getPosition())
        self.assertEqual(Position(1, 1), state.getShips("a1")[1].getPosition())
        self.assertEqual(Ship.ORIENTATION_0_DEG, state.getShips("a1")[0].getOrientation())
        self.assertEqual(Ship.ORIENTATION_0_DEG, state.getShips("a1")[1].getOrientation())

        # check torpedos for deep copy
        self.assertTrue(copied.getTorpedos("a1")[0] is not state.getTorpedos("a1")[0])
        self.assertTrue(copied.getTorpedos("a1")[1] is not state.getTorpedos("a1")[1])
        self.assertEqual(len(copied.getTorpedos("a1")), len(state.getTorpedos("a1")))

    def test_GetNextAgentToMove(self):
        state = State(["a1", "a2", "a3"], {"a1":Grid(1,1), "a2":Grid(1,1), "a3":Grid(1,1)}, {"a1":[], "a2":[], "a3":[]}, {"a1":[], "a2":[], "a3":[]})
        self.assertEqual("a1", state.currentAgent())
        state.setNextAgentToMove()
        self.assertEqual("a2", state.currentAgent())
        state.setNextAgentToMove()
        self.assertEqual("a3", state.currentAgent())
        state.setNextAgentToMove()
        self.assertEqual("a1", state.currentAgent())

    def test_GetOpponents(self):
        state = State(["a1", "a2", "a3"], {"a1":Grid(1,1), "a2":Grid(1,1), "a3":Grid(1,1)}, {"a1":[], "a2":[], "a3":[]}, {"a1":[], "a2":[], "a3":[]})
        self.assertEqual(collections.Counter(["a2","a3"]), collections.Counter(state.getOpponents("a1")))
        self.assertEqual(collections.Counter(["a1","a3"]), collections.Counter(state.getOpponents("a2")))
        self.assertEqual(collections.Counter(["a1","a2"]), collections.Counter(state.getOpponents("a3")))
        

