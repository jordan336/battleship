from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
import random

class HuntAndTargetAgent(Agent):

    def __init__(self, name, rules):
        self.name = name

        #TODO: remove
        self.rules = rules
   
    def placeShip(self, ship): 
        raise NotImplementedError()

    def getAction(self, state): 

        #TODO: should get the torpedos from the state, not the rules.
        (torpedo, torpedoCount) = (self.rules.getTorpedos(None))[0]

        #self.drawCurrentState(state)
        board = state.getBoards()[0]
        candidateActions = []
        legalMoves = state.legalTargets()
        for hitPos in board.getHitPositions():
            for adjacentTile in board.getValidNeighbors(hitPos):
                if adjacentTile not in board.getMissedPositions() and adjacentTile in legalMoves:
                    candidateActions.append(adjacentTile)
                    
        if not candidateActions:
            candidateActions = legalMoves
        
        #TODO: Should not be hardcoding board 0 as the target
        action = TorpedoAction(torpedo, random.choice(candidateActions), 0)
        return action

    def incorporateFeedback(self, state, action, reward, newState):
        pass


