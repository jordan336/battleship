from Agent import Agent
from Position import Position
import Util

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

