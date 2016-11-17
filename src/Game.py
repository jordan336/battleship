
from Position import Position
from Grid import Grid
from State import State
from Action import Action
from Rules import Rules
from TextDisplay import TextDisplay
import random

"""
    The Game manages the control flow, soliciting actions from agents.
"""
class Game:


    def __init__(self, rules, agents=[]):
        self.rules = rules
        self.agents = agents
        
    def drawCurrentState(self):
        board = self.currentState.getBoards()[0]
        ships = self.currentState.getShips()
        TextDisplay.draw(board, ships, True) 
        
    def placeShips(self, board, ships):
        placedShips = []
        #TextDisplay.draw(board, placedShips, True)
        for ship in ships:
            fits = False
            while not fits:
                tryPos = Position(random.randint(0, board.getWidth() - 1), random.randint(0, board.getHeight() - 1))
                orientations = ['0', '90', '180', '270']
                random.shuffle(orientations)
                for orientation in orientations:
                    if self.shipFits(board, placedShips, ship.getLength(), tryPos, orientation):
                        ship.place(tryPos, orientation)
                        placedShips.append(ship)
                        #print ship.getLength(), tryPos, orientation
                        #TextDisplay.draw(board, placedShips, True)
                        fits = True
                    
    def shipFits(self, board, placedShips, length, headPosition, orientation):
        (x, y) = headPosition.getPosition()
        for i in range(length):
            if (x < 0) or (y < 0) or (x > board.getWidth() -1) or (y > board.getHeight() -1):
                return False
            for placedShip in placedShips:
                if placedShip.hasShip(Position(x, y)):
                    return False
            if orientation == '0':
                x += 1
            elif orientation == '90':
                y += 1
            elif orientation == '180':
                x -= 1
            else:
                y -= 1
        return True
        

    def startState(self):
        boards = self.rules.getBoards()
        ships = self.rules.getShips()
        (torpedo, torpedoCount) = (self.rules.getTorpedos())[0]
        self.placeShips(boards[0], ships)
        newState = State(boards, ships, torpedo, 1)
        return newState
        
    def run(self):
        self.currentState = self.startState()
        while not self.currentState.isEnd():
            #self.drawCurrentState()
            currentAgent = self.currentState.currentAgent()
            action = self.agents[currentAgent].getAction(self.currentState)
            self.currentState.generateSuccessor(action, currentAgent)
        print 'Game over! Here is the final game board:'
        self.drawCurrentState()

 