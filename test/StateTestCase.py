import unittest
from State import State
from Grid import Grid

class StateTestCase(unittest.TestCase):

    def test_Create(self):
        board = Grid(10, 10)
        state = State([board], [[]], [[]], 1)

        self.assertEqual(board, state.getBoards()[0])
        self.assertEqual([[]], state.getShips())
        self.assertEqual([[]], state.getTorpedos())
        self.assertEqual(0, state.currentAgent())

    # TODO: enable when State.py is fixed with list of lists
    """ 
    def test_BadCreate(self):
        # added agents, but no boards, ships, torpedos
        with self.assertRaises(RuntimeError):
            state = State([], [], [], 3)
    
        # ...
    """
        

