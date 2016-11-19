
from Action import Action
from Position import Position

"""
State

Class representing the current game state, including each Agent's ships
and torpedos.  The State should contain all information necessary for
an Agent to make a decision about how to act.

TODO: Each Agent should have statistics, like number of total shots, number of 
      hits, etc.
"""
class State:

    """
    init()

    Create a new state.

    - gameBoards: List of Grids, one for each Agent.  The Grid for an agent
                  is the Grid with that Agent's ships.
                  TODO: This scheme wont work with more than 2 players.

    - ships     : List of list of Ships, one list for each Agent.

    - torpedos  : List of list of Torpedos, one list for each Agent.  The list
                  of torpedos is the list of torpedos the Agent has yet to fire.

    - numAgents : The total number of agents 
    """
    def __init__(self, gameBoards, ships, torpedos, numAgents):
        self.gameBoards = gameBoards
        self.ships = ships
        self.torpedos = torpedos
        self.numAgents = numAgents
        self.nextAgentToMove= 0
        self.scores = []
        self.moveCounts = []
        for i in range(numAgents):
            self.scores.append(0)
            self.moveCounts.append(0)

        # TODO
        """
        # Ships and torpedos should be a list of lists.  Each agent should have a list of
        # torpedos and ships.  Fix this and then enable the below check.

        # check the length of the input lists
        if self.numAgents < 0 or \
           len(self.gameBoards) != numAgents or \
           len(self.ships) != numAgents or \
           len(self.torpedos) != numAgents:
            raise RuntimeError("Incorrect state inputs")
        """
    def getBoards(self):
        return self.gameBoards

    def getShips(self):
        return self.ships

    def getTorpedos(self):
        return self.torpedos

    def currentAgent(self):
        return self.nextAgentToMove
        
    """
    isEnd()

    For every agent's list of ships, check if any ship is not sunk.
    If the every ship for an agent is sunk, return true.  Otherwise,
    all agents have at least one non-sunk ship and return false.
    """
    def isEnd(self):
        agentSunk = True
        for ship in self.ships:
            if not ship.isSunk():
                agentSunk = False
        if agentSunk:
            return True
        return False
    

    """
    getScore()

    Return a number representing the current game score for the given agent.
    Currently, add up the score from every opponent ship.

    TODO: This doesn't work if we have more than 2 Agents.  Instead, we should
          base the score on the Agent's statisitics, see above comment.

    - agentIndex: The Agent's score to get (between 0 and self.numAgents-1)
    """
    def getScore(self, agentIndex):
        return self.scores[agentIndex] 
 
    """
    calcScore()

    Return a number representing the current game score for the given agent.
    Currently, add up the score from every opponent ship.

    TODO: This doesn't work if we have more than 2 Agents.  Instead, we should
          base the score on the Agent's statisitics, see above comment.

    - agentIndex: The Agent's score to get (between 0 and self.numAgents-1)
    """
    def calcScore(self, agentIndex):
        score = 0
        for ship in self.ships:
            score += ship.getScore()
        score -= self.moveCounts[agentIndex]
        self.scores[agentIndex] = score

    """
    getMoveCount()

    Return a number representing the number moves taken.

    TODO: This doesn't work if we have more than 2 Agents.  Instead, we should
          base the score on the Agent's statisitics, see above comment.

    - agentIndex: The Agent's score to get (between 0 and self.numAgents-1)
    """
    def getMoveCount(self, agentIndex):
        return self.moveCounts[agentIndex] 

    """
    actions()

    Return a list of legal target positions for the current state.

    - agentIndex: The Agent's board to get (which holds the Agent's ships)
    """        
    def legalTargets(self, agentIndex=0):
        legalTargets = []
        missedPos = self.gameBoards[agentIndex].getMissedPositions()
        hitPos = self.gameBoards[agentIndex].getHitPositions()
        for i in range(self.gameBoards[agentIndex].width):
            for k in range(self.gameBoards[agentIndex].height):
                if Position(i, k) not in missedPos and Position(i, k) not in hitPos :
                    legalTargets.append(Position(i, k))
        return legalTargets
                

    """
    generateSuccessor()
    
    Given an Action, generate a new State representing the game after the
    Action is executed.
    """
    def generateSuccessor(self, action, agentIndex=0, verbose=False):
        if action.getType() == Action.ACTION_TYPE_FIRE_TORPEDO:
            if verbose: print "Action: Firing torpedo at: ", action.getTarget()
            hit = False
            for ship in self.ships:
                shipHitIndex = ship.shipSegmentIndex(action.getTarget())
                if shipHitIndex >= 0:
                    hit = True
                    if verbose: print ship.getName() + " has been hit!!"
                    self.gameBoards[agentIndex].setHitPosition(action.getTarget())
                    ship.takeDamage(shipHitIndex)
                    if verbose: 
                        if ship.getDamage() == 0:
                            print ship.getName() + " has been sunk!!" 
                        else:
                            print "Ship's hit points remaining: ", ship.getDamage()
                    break
            if not hit:
                if verbose: print "Missed!!"
                self.gameBoards[agentIndex].setMissedPosition(action.getTarget())
            #UpdateScores
            self.moveCounts[agentIndex] += 1
            self.calcScore(agentIndex)
            # TODO
        else:
            print "Other action"

