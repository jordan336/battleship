
class State:

    def __init__(self, gameBoard, ships, torpedos, numAgents):
        self.gameBoard = gameBoard
        self.ships = ships
        self.torpedos = torpedos
        self.numAgents = numAgents
        self.nextAgentToMove= 0

    def isEnd(self):
        #TODO
    
    def getScore(self, agentIndex):
        # TODO

    def generateSuccessor(self, action):
        # TODO

