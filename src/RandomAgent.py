from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
import random

class RandomAgent(Agent):

    def __init__(self, name, rules):
        self.name = name
        self.rules = rules
   
    def placeShip(self, ship): 
        raise NotImplemented

    def getAction(self, state): 
        (torpedo, torpedoCount) = (self.rules.getTorpedos())[0]
        candidateActions = state.legalTargets()
        action = TorpedoAction(torpedo, random.choice(candidateActions))
        return action


