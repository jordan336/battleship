import copy
from Action import Action
from Position import Position

"""
State

Class representing the current game state, including each Agent's ships
and torpedos.  The State should contain all information necessary for
an Agent to make a decision about how to act.
"""
class State:

    """
    init()

    Create a new state.  There must be at least 2 Agents playing.  There can 
    be 0 Agents in the special case that a blank State is being create in
    deepCopy().

    - agents     : The names of the Agents playing the game

    - gameBoards : Dictionary of Grids, one for each Agent.  The Grid for an agent
                   is the Grid with that Agent's ships.

    - ships      : Dictionary of list of Ships, one list for each Agent.

    - torpedos   : Dictionary of list of (Torpedo, count) tuples, one list for each Agent.  The list
                   of torpedos is the list of torpedos the Agent has yet to fire.
    """
    def __init__(self, agents, gameBoards, ships, torpedos):
        if len(agents) < 2 and len(agents) != 0:
            raise RuntimeError("At least 2 Agents must play")

        self.agents = agents
        self.gameBoards = gameBoards
        self.ships = ships
        self.torpedos = torpedos
        self.winner = None
        self.scores = {}
        self.moveCounts = {}
        for agent in agents:
            self.scores[agent] = 0
            self.moveCounts[agent] = 0

        if len(agents) == 0:
            self.nextAgentToMove = None
        else:
            self.nextAgentToMove = agents[0]

        # check the length of the inputs
        if len(self.gameBoards) != len(agents) or \
           len(self.ships) != len(agents) or \
           len(self.torpedos) != len(agents):
            raise RuntimeError("Incorrect state inputs")

    def deepCopy(self):
        state = State([], {}, {}, {})
        for agent in self.agents:
            state.agents.append(copy.deepcopy(agent))
        for agent, board in self.gameBoards.iteritems():
            state.gameBoards[agent] = copy.deepcopy(board)
        for agent, shipList in self.ships.iteritems():
            state.ships[agent] = copy.deepcopy(shipList)
        for agent, torpedoList in self.torpedos.iteritems():
            state.torpedos[agent] = copy.deepcopy(torpedoList)
        for agent, score in self.scores.iteritems():
            state.scores[agent] = score
        for agent, moveCount in self.moveCounts.iteritems():
            state.moveCounts[agent] = score
        state.nextAgentToMove = self.nextAgentToMove
        return state
        
    def getAgents(self):
        return self.agents

    def getBoard(self, agentName = None):
        if agentName is not None:
            return self.gameBoards[agentName]
        else:
            return self.gameBoards

    def getShips(self, agentName = None):
        if agentName is not None:
            return self.ships[agentName]
        else:
            return self.ships

    def getTorpedos(self, agentName = None):
        if agentName is not None:
            return self.torpedos[agentName]
        else:
            return self.torpedos

    def getWinner(self):
        return self.winner

    def currentAgent(self):
        return self.nextAgentToMove

    def setNextAgentToMove(self):
        agentNames = [agent for agent in self.agents]
        curIndex = agentNames.index(self.nextAgentToMove)
        nextIndex = (curIndex + 1) % len(self.agents)
        self.nextAgentToMove = self.agents[nextIndex]

    def getOpponents(self, agentName):
        return [agent for agent in self.agents if agent != agentName]
        
    """
    isEnd()

    For every agent's list of ships, check if any ship is not sunk.
    If the every ship for an agent is sunk, return true.  Otherwise,
    all agents have at least one non-sunk ship.  Also, check if every
    agent has at least 1 torpedo left to fire, otherwise return true.

    Update self.winner with the winner of the game, if this is an end
    state.  The winner has the maximum score and at least 1 torpedo 
    and at least 1 unsunk ship.
    """
    def isEnd(self):

        # Check if all ships sunk
        for agent, shipList in self.ships.iteritems():
            agentSunk = True
            for ship in shipList:
                if not ship.isSunk():
                    agentSunk = False
            if agentSunk:
                winScores = copy.deepcopy(self.scores)
                del winScores[agent]
                self.winner = max(winScores, key=winScores.get)
                return True

        # Check if out of torpedos
        for agent, torpedoList in self.torpedos.iteritems():
            sumTorpedos = 0
            for (torpedo, count) in torpedoList.iteritems():
                sumTorpedos += count
            if sumTorpedos <= 0:
                winScores= copy.deepcopy(self.scores)
                del winScores[agent]
                self.winner = max(winScores, key=winScores.get)
                return True

        return False
    
    """
    getScore()

    Return a number representing the current game score for the given agent.
    Currently, add up the score from every opponent ship.

    TODO: This doesn't work if we have more than 2 Agents.  Instead, we should
          base the score on the Agent's statisitics, see above comment.

    - agentName: The Agent's score to get 
    """
    def getScore(self, agentName):
        return self.scores[agentName] 
 
    """
    calcScore()

    Return a number representing the current game score for the given agent.
    Currently, add up the score from every opponent ship.

    - agentName: The Agent's score to get
    """
    def calcScore(self, agentName):
        score = 0
        for opponent in self.getOpponents(agentName):
            for ship in self.ships[opponent]:
                score += ship.getScore()
        score -= self.moveCounts[agentName]
        self.scores[agentName] = score

    """
    getMoveCount()

    Return a number representing the number moves taken.

    - agentName: The Agent's score to get
    """
    def getMoveCount(self, agentName):
        return self.moveCounts[agentName] 

    """
    getHitCount()

    Return a number representing the number of successful hits.

    - agentName: The Agent's hit count to get
    """
    def getHitCount(self, agentName):
        hitCount = 0
        for ship in self.getShips(agentName):
            hitCount += ship.getHits()
        return hitCount
        
    """
    legalTargets()

    Return a list of legal target positions for attacking the given Agent
    in the current state.

    - agentName: The Agent's board to get (which holds the Agent's ships)
    """        
    def legalTargets(self, agentName):
        legalTargets = []
        missedPos = self.gameBoards[agentName].getMissedPositions()
        hitPos = self.gameBoards[agentName].getHitPositions()
        for i in range(self.gameBoards[agentName].width):
            for k in range(self.gameBoards[agentName].height):
                if Position(i, k) not in missedPos and Position(i, k) not in hitPos :
                    legalTargets.append(Position(i, k))
        return legalTargets

    """
    generateSuccessor()
    
    Given an Action, generate a new State representing the game after the
    Action is executed.

    - action          : Action to take

    - actingAgentName : The Agent taking the Action

    - verbose         : Verbosity for print statements
    """
    def generateSuccessor(self, action, actingAgentName, verbose=False):
        if action is None:
            if verbose: print "Agent did not act"

        elif action.getType() == Action.ACTION_TYPE_FIRE_TORPEDO:
            targetAgentName = action.getTargetAgentName()
            targetPosition = action.getTarget()
            torpedo = action.getTorpedo()

            # Make sure the agent has enough torpedos
            if self.torpedos[actingAgentName][torpedo] <= 0:
                print "Agent ", actingAgentName, " tried to fire a nonexistent torpedo"
                return

            if verbose: print "Action: Firing torpedo at: ", targetPosition, " target agent: ", targetAgentName

            hit = False
            for ship in self.ships[targetAgentName]:
                for shipPosition in ship.getPositions():
                    damage = torpedo.getDamage(targetPosition, shipPosition)
                    if damage > 0:
                        hit = True
                        if verbose: print ship.getName() + " has been hit!!"
                        #TODO: setHitPosition should take the damage
                        self.gameBoards[targetAgentName].setHitPosition(shipPosition)
                        ship.takeDamage_Position(shipPosition, damage)
                        if verbose: 
                            if ship.getDamage() == 0:
                                print ship.getName() + " has been sunk!!" 
                            else:
                                print "Ship's hit points remaining: ", ship.getDamage()

            if not hit:
                if verbose: print "Missed!!"
                self.gameBoards[targetAgentName].setMissedPosition(targetPosition)

            # Update scores
            self.moveCounts[actingAgentName] += 1
            self.calcScore(actingAgentName)

            # Decrement remaining torpedos
            self.torpedos[actingAgentName][torpedo] -= 1

        else:
            print "Other action"

        # Next agent's turn
        self.setNextAgentToMove()

