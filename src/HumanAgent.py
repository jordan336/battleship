from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
from TextDisplay import TextDisplay

class HumanAgent(Agent):

    def __init__(self, name):
        self.name = name
   
    def drawCurrentState(self, state):
        #TODO Should not hardcode 0, only works with 1 opponent.
        opponentToAttack = state.getOpponents(self.name)[0]
        board = state.getBoard(opponentToAttack)
        ships = state.getShips(opponentToAttack)
        TextDisplay.draw(board, ships, True) 
   
    def placeShip(self, ship): 
        raise NotImplementedError()

    def getAction(self, state): 

        #TODO Should not hardcode 0, only works with 1 opponent.
        opponentToAttack = state.getOpponents(self.name)[0]

        self.drawCurrentState(state)
        while True:
            print 'Hello human', self.name, '! Please provide x and y coordinates of your target.'

            # get position to shoot
            x = input('Enter target x: ')
            y = input('Enter target y: ')
            # TODO: type check user input
            inputPos = Position(x, y)
            if inputPos in state.legalTargets(opponentToAttack):

                while True:
                    # get torpedo to fire
                    allowedIndices = []

                    for index, (torpedo, count) in enumerate(state.getTorpedos(self.name)):
                        if count > 0:
                            print index, ': ', torpedo.getTorpedoType(), '[', count, ']'
                            allowedIndices.append(index)

                    torpedoIndex = input('Enter the torpedo index: ')
                    if torpedoIndex in allowedIndices:
                        action = TorpedoAction(state.getTorpedos(self.name)[torpedoIndex][0], inputPos, opponentToAttack)
                        return action

                    else:
                        print 'Invalid torpedo; please try again.'

            else:
                print 'Invalid target; please try again.'

    def incorporateFeedback(self, state, action, reward, newState):
        pass

