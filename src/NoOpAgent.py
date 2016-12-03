from Agent import Agent
from Position import Position

class NoOpAgent(Agent):

    def __init__(self, name):
        self.name = name
   
    def placeShip(self, ship): 
        raise NotImplementedError()

    def getAction(self, state): 
        pass

    def incorporateFeedback(self, state, action, reward, newState):
        pass

    def prepareForTesting(self):
        pass

