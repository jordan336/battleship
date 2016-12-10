from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
import random
import Util

class HuntAndTargetAgent(Agent):

    def __init__(self, name):
        self.name = name

    def placeShips(self, board, ships): 
        Util.randomPlaceShips(board, ships)

    def getAction(self, state): 
        randomTorpedo = random.choice(state.getTorpedos(self.name).keys())
        opponentToAttack = random.choice(state.getOpponents(self.name))

        board = state.getBoard(opponentToAttack)
        candidateActions = []
        legalMoves = state.legalTargets(opponentToAttack)
        for hitPos in board.getHitPositions():
            for adjacentTile in board.getValidNeighbors(hitPos):
                if adjacentTile not in board.getMissedPositions() and adjacentTile in legalMoves:
                    candidateActions.append(adjacentTile)
                    
        if not candidateActions:
            candidateActions = legalMoves
        
        action = TorpedoAction(randomTorpedo, random.choice(candidateActions), opponentToAttack)
        return action

    def incorporateFeedback(self, state, action, reward, newState):
        pass

    def prepareForTesting(self):
        pass

