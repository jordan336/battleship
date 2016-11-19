from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
import random

class RandomAgent(Agent):

    def __init__(self, name, rules):
        self.name = name
        #TODO: remove
        self.rules = rules
   
    def placeShip(self, ship): 
        raise NotImplementedError()

    def getAction(self, state): 
        #TODO: torpedos should come from state, not rules
        (torpedo, torpedoCount) = (self.rules.getTorpedos(None))[0]
        candidateActions = state.legalTargets()
        #TODO should not be hardcoding 0
        action = TorpedoAction(torpedo, random.choice(candidateActions), 0)
        return action

    def incorporateFeedback(self, state, action, reward, newState):
        pass

