from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
from TextDisplay import TextDisplay

class HumanAgent(Agent):

    def __init__(self, name, rules):
        self.name = name
        #TODO: remove
        self.rules = rules
   
    def drawCurrentState(self, state):
        #TODO Should not hardcode 0, only works with 1 opponent.
        opponentToAttack = state.getOpponents(self.name)[0]
        board = state.getBoard(opponentToAttack)
        ships = state.getShips(opponentToAttack)
        TextDisplay.draw(board, ships, True) 
   
    def placeShip(self, ship): 
        raise NotImplementedError()

    def getAction(self, state): 

        #TODO: torpedos should come from state, not rules
        (torpedo, torpedoCount) = (self.rules.getTorpedos(None))[0]

        #TODO Should not hardcode 0, only works with 1 opponent.
        opponentToAttack = state.getOpponents(self.name)[0]

        self.drawCurrentState(state)
        while True:
            print 'Hello human', self.name, '! Please provide x and y coordinates of your target.'
            x = input('Enter target x: ')
            y = input('Enter target y: ')
            # TODO: type check user input
            inputPos = Position(x, y)
            if inputPos in state.legalTargets(opponentToAttack):
                break
            else:
                print 'Invalid target; please try again.'

        action = TorpedoAction(torpedo, inputPos, opponentToAttack)
        return action

    def incorporateFeedback(self, state, action, reward, newState):
        pass

