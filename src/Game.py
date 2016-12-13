from Position import Position
from State import State
from TextDisplay import TextDisplay
from HumanAgent import HumanAgent
from Statistics import Statistics

"""
    The Game manages the control flow, soliciting actions from agents.
"""
class Game:

    def __init__(self, rules, agents=[], stats=None, useSameState=False):
        self.rules = rules
        self.agents = agents
        self.stats = stats
        self.useSameState = useSameState
        if self.useSameState:
            self.sameInitialState = self.startState()
        
    def drawCurrentState(self):
        for agent in self.currentState.getAgents():
            print 'Agent: ', agent
            board = self.currentState.getBoard(agent)
            ships = self.currentState.getShips(agent)
            TextDisplay.draw(board, ships, True) 

    def getAgentIndex(self, agentName):
        for index, agent in enumerate(self.agents):
            if agent.getName() == agentName:
                return index
        raise RuntimeError("Agent " + agentName + " not in agents list")
 
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
            agent.placeShips(board, shipList)
        newState = State(agentNames, boards, ships, torpedos)
        return newState
        
    def run(self):

        # Get the initial state.
        if self.useSameState:
            self.currentState = self.sameInitialState.deepCopy()
        else:
            self.currentState = self.startState()

        # run the game
        while not self.currentState.isEnd():
            currentAgentName = self.currentState.currentAgent()
            currentAgentIndex = self.getAgentIndex(currentAgentName)

            if type(self.agents[currentAgentIndex]) is HumanAgent:
                verbose = True
            else: 
                verbose = False

            action = self.agents[currentAgentIndex].getAction(self.currentState)
            oldState = self.currentState.deepCopy()
            self.currentState.generateSuccessor(action, currentAgentName, verbose)
            newState = self.currentState.deepCopy()
            reward = newState.getScore(currentAgentName) - oldState.getScore(currentAgentName)

            # Inform learning agents of s, a, r, s
            self.agents[currentAgentIndex].incorporateFeedback(oldState, action, reward, newState)

            # Update statistics
            if self.stats is not None:
                self.stats.logAgentTurn(self.agents[currentAgentIndex].getName(), oldState, action, reward, newState)

        print 'Game over! Here is the final game board:'
        self.drawCurrentState()

        # Return total number of moves, final score, and win boolean for each agent
        returnStats = {}
        for agent in self.currentState.getAgents():
            moves = self.currentState.getMoveCount(agent)
            score = self.currentState.getScore(agent)
            win = (self.currentState.getWinner() == agent)
            returnStats[agent] = (moves, score, win)
        return returnStats

