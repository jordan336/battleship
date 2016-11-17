from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
from TextDisplay import TextDisplay
import random

class HuntAndTargetAgent(Agent):

    def __init__(self, name, rules):
        self.name = name
        self.rules = rules
   
    def drawCurrentState(self, state):
        board = state.getBoards()[0]
        ships = state.getShips()
        TextDisplay.draw(board, ships, True) 
   
    def placeShip(self, ship): 
        raise NotImplemented

    def getAction(self, state): 
        (torpedo, torpedoCount) = (self.rules.getTorpedos())[0]
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
        
        action = TorpedoAction(torpedo, random.choice(candidateActions))
        return action


