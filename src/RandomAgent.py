from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
import random

class RandomAgent(Agent):

    def __init__(self, name):
        self.name = name
   
    def placeShip(self, ship): 
        raise NotImplementedError()

    def getAction(self, state): 
        randomTorpedo = random.choice(state.getTorpedos(self.name).keys())
        opponents = state.getOpponents(self.name)
        opponentToAttack = random.choice(opponents)
        candidateActions = state.legalTargets(opponentToAttack)
        action = TorpedoAction(randomTorpedo, random.choice(candidateActions), opponentToAttack)
        return action

    def incorporateFeedback(self, state, action, reward, newState):
        pass

    def prepareForTesting(self):
        pass

