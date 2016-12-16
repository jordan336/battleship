from Agent import Agent
from Position import Position
import Util

"""
NoOpAgent implementing the Agent interface

This Agent takes no action and randomly places
its ships.  This Agent is used as an opponent
when testing another Agent individually.
"""
class NoOpAgent(Agent):

    def __init__(self, name):
        self.name = name
   
    def placeShips(self, board, ships): 
        Util.randomPlaceShips(board, ships)

    def getAction(self, state): 
        pass

    def incorporateFeedback(self, state, action, reward, newState):
        pass

    def prepareForTesting(self):
        pass

