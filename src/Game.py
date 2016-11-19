
from Position import Position
from State import State
from TextDisplay import TextDisplay
import random
from HumanAgent import HumanAgent

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
 
 
    """
        placeShips()

        Given a game board and list of ships, place the ships on the game board randomly and assign each ship with corresponding positions and orientations. 

        TODO: This is temporarily implemented in the Game module. It should be removed eventually and the work should be performed by game agents, either randomly, by AI or manually.

    """
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

    """
        placeShips()

        Used by placeShips() to determine whether the ship with given length and position/orientation will fit on the game board. Return false if the ship will overlap with an existing ship that has already been placed, or falls out of the board's range. 

        TODO: This is temporarily implemented in the Game module. It should be removed eventually and the work should be performed by game agents, either randomly, by AI or manually.
    """                        
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
        boards = []
        ships = []
        torpedos = []
        for agent in self.agents:
            board = self.rules.getBoard(agent)
            shipList = self.rules.getShips(agent)
            torpedoList = self.rules.getTorpedos(agent)
            boards.append(board)
            ships.append(shipList)
            torpedos.append(torpedoList)
            self.placeShips(board, shipList)
        newState = State(boards, ships, torpedos, 1)
        return newState
        
    def run(self):
        self.currentState = self.startState()
        while not self.currentState.isEnd():
            #self.drawCurrentState()
            currentAgent = self.currentState.currentAgent()
            if type(self.agents[currentAgent]) is HumanAgent:
                verbose = True
            else: 
                verbose = False

            action = self.agents[currentAgent].getAction(self.currentState)
            oldState = self.currentState.deepCopy()
            self.currentState.generateSuccessor(action, currentAgent, verbose)
            newState = self.currentState.deepCopy()

            #TODO: a different reward calculate?
            reward = newState.getScore(currentAgent) - oldState.getScore(currentAgent)

            # Inform learning agents of s, a, r, s
            self.agents[currentAgent].incorporateFeedback(oldState, action, reward, newState)

        print 'Game over! Here is the final game board:'
        self.drawCurrentState()
        finalNumMoves = self.currentState.getMoveCount(currentAgent)
        finalScore = self.currentState.getScore(currentAgent)
        print 'Moves:', finalNumMoves, 'Score:', finalScore
        return finalNumMoves, finalScore

 
