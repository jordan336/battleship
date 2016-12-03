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
        for agent in self.currentState.getAgents():
            board = self.currentState.getBoard(agent)
            ships = self.currentState.getShips(agent)
            TextDisplay.draw(board, ships, True) 

    def getAgentIndex(self, agentName):
        for index, agent in enumerate(self.agents):
            if agent.getName() == agentName:
                return index
        raise RuntimeError("Agent " + agentName + " not in agents list")
 
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
    shipFits()

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
        agentNames = []
        boards = {}
        ships = {}
        torpedos = {}
        for agent in self.agents:
            agentNames.append(agent.getName())
            board = self.rules.getBoard(agent)
            shipList = self.rules.getShips(agent)
            torpedoList = self.rules.getTorpedos(agent)
            boards[agent.getName()] = board
            ships[agent.getName()] = shipList
            torpedos[agent.getName()] = torpedoList
            self.placeShips(board, shipList)
        newState = State(agentNames, boards, ships, torpedos)
        return newState
        
    def run(self):
        self.currentState = self.startState()
        while not self.currentState.isEnd():
            currentAgentName = self.currentState.currentAgent()
            currentAgentIndex = self.getAgentIndex(currentAgentName)

            #self.drawCurrentState()

            if type(self.agents[currentAgentIndex]) is HumanAgent:
                verbose = True
            else: 
                verbose = False

            action = self.agents[currentAgentIndex].getAction(self.currentState)
            oldState = self.currentState.deepCopy()
            self.currentState.generateSuccessor(action, currentAgentName, verbose)
            newState = self.currentState.deepCopy()
            #TODO: a different reward calculation?
            reward = newState.getScore(currentAgentName) - oldState.getScore(currentAgentName)

            # Inform learning agents of s, a, r, s
            self.agents[currentAgentIndex].incorporateFeedback(oldState, action, reward, newState)


        print 'Game over! Here is the final game board:'
        self.drawCurrentState()
        #TODO doesnt work with more than 1 agent
        agent = self.currentState.getAgents()[0]
        finalNumMoves = self.currentState.getMoveCount(agent)
        finalScore = self.currentState.getScore(agent)
        print 'Moves:', finalNumMoves, 'Score:', finalScore

        return finalNumMoves, finalScore  #TODO: return array of final scores

 
