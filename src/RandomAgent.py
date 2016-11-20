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
        opponents = state.getOpponents(self.name)
        opponentToAttack = random.choice(opponents)
        candidateActions = state.legalTargets(opponentToAttack)
        action = TorpedoAction(torpedo, random.choice(candidateActions), opponentToAttack)
        return action

    def incorporateFeedback(self, state, action, reward, newState):
        pass

