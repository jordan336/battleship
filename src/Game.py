from Position import Position
from State import State
from TextDisplay import TextDisplay
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

 
