from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
import random

class HuntAndTargetAgent(Agent):

    def __init__(self, name):
        self.name = name

    def placeShip(self, ship): 
        raise NotImplementedError()

    def getAction(self, state): 
        (torpedo, torpedoCount) = random.choice(state.getTorpedos(self.name))

        #self.drawCurrentState(state)
    
        #TODO: setting 0 only works for 1 opponent
        opponentToAttack = state.getOpponents(self.name)[0]

        board = state.getBoard(opponentToAttack)
        candidateActions = []
        legalMoves = state.legalTargets(opponentToAttack)
        for hitPos in board.getHitPositions():
            for adjacentTile in board.getValidNeighbors(hitPos):
                if adjacentTile not in board.getMissedPositions() and adjacentTile in legalMoves:
                    candidateActions.append(adjacentTile)
                    
        if not candidateActions:
            candidateActions = legalMoves
        
        action = TorpedoAction(torpedo, random.choice(candidateActions), opponentToAttack)
        return action

    def incorporateFeedback(self, state, action, reward, newState):
        pass

