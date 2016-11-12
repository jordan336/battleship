
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


    """
    isEnd()

    For every agent's list of ships, check if any ship is not sunk.
    If the every ship for an agent is sunk, return true.  Otherwise,
    all agents have at least one non-sunk ship and return false.
    """
    def isEnd(self):
        for agentShips in self.ships:
            agentSunk = True
            for ship in agentShips:
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
        score = 0
        for agentInd in range(self.numAgents):
            if agentInd == agentIndex:
                continue
            for ship in self.ships[agentInd]:
                score += ship.getScore()
        return score
        
    """
    hasShip(self, position)

    Return a list of legal target positions for the current state.

    """ 

    """
    actions()

    Return a list of legal target positions for the current state.

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
    def generateSuccessor(self, action, agentIndex=0):
        if action.getType() == Action.ACTION_TYPE_FIRE_TORPEDO:
            torpedo = action.getTorpedo()
            print "Action: Firing torpedo at: ", torpedo.getTargetPosition()
            for ship in self.ships:
                if ship.hasShip(torpedo.getTargetPosition()):
                    print "Hit!!"
                    self.gameBoards[agentIndex].setHitPosition(torpedo.getTargetPosition())
                else:
                    print "Missed!!"
                    self.gameBoards[agentIndex].setMissedPosition(torpedo.getTargetPosition())
            # TODO
        else:
            print "Other action"

