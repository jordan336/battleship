from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
from TextDisplay import TextDisplay

class HumanAgent(Agent):

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
        self.drawCurrentState(state)
        while True:
            print 'Hello human', self.name, '! Please provide x and y coordinates of your target.'
            x = input('Enter target x: ')
            y = input('Enter target y: ')
            inputPos = Position(x, y)
            if inputPos in state.legalTargets():
                break
            else:
                print 'Invalid target; please try again.'
        action = TorpedoAction(torpedo, inputPos)
        return action

