from collections import defaultdict
from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
import random
import math
import Util

"""
identityFeatureExtractor()

Rote learning feature extractor.
"""
def identityFeatureExtractor(state, action):
    featureKey = (state, action)
    featureValue = 1
    return [(featureKey, featureValue)]


"""
featureExtractor()

More advanced feature extractor, intended for all uses.
"""
def featureExtractor(state, action):
    features = []
    sunkPositions = []
    targetX = action.getTarget().x
    targetY = action.getTarget().y
    opponentBoard = state.getBoard(action.getTargetAgentName())
    opponentShips = state.getShips(action.getTargetAgentName())
    for ship in opponentShips:
        if ship.isSunk():
            sunkPositions += ship.getPositions()

    # Decide if we are hunting for a new target, or if an opponent ship is damaged
    hunting = True
    for ship in opponentShips:
        if not ship.isSunk() and ship.getHits() > 0:
            hunting = False

    # Horizontal distance to the nearest hit square, excluding sunk ships
    # exclude feature when there are no hits on the row
    hitRowDist = opponentBoard.getDistNearestSameRowHit(targetX, targetY, sunkPositions)
    if hitRowDist != -1:
        features.append(('hitRowDist='+str(hitRowDist), 1))

    # Vertical distance to the nearest hit square, excluding sunk ships
    # exclude feature when there are no hits on the column
    hitColDist = opponentBoard.getDistNearestSameColHit(targetX, targetY, sunkPositions)
    if hitColDist != -1:
        features.append(('hitColDist='+str(hitColDist), 1))

    # continuous hits if targeting
    if not hunting:
        continuousVerticalHits = opponentBoard.getContinuousVerticalHits(targetX, targetY)
        continuousHorizontalHits = opponentBoard.getContinuousHorizontalHits(targetX, targetY)
        maxContiguousHits = max(continuousVerticalHits, continuousHorizontalHits)
        if maxContiguousHits != 1:
            features.append(('contiguousHits='+str(maxContiguousHits), 1))

    # percentage of opponent unhit ships that fit in the unexplored regions
    if hunting:
        leftHorMissedLen = opponentBoard.getLeftHorizontalMissedLength(targetX, targetY)
        rightHorMissedLen = opponentBoard.getRightHorizontalMissedLength(targetX, targetY)
        upVerMissedLen = opponentBoard.getUpVerticalMissedLength(targetX, targetY)
        downVerMissedLen = opponentBoard.getDownVerticalMissedLength(targetX, targetY)
        percentageUnhitShipsFit = Util.percentageUnhitShipsFit(opponentShips, rightHorMissedLen, leftHorMissedLen, upVerMissedLen, downVerMissedLen)
        features.append(('percentageUnhitShipsFit', percentageUnhitShipsFit))

    return features

"""
QLearningAgent implementing the Agent interface

An implementation of the QLearning reinforcement learning 
algorithm with function approximation.  This Agent will
learn the optimal policy when playing the Battleship game.
"""
class QLearningAgent(Agent):

    def __init__(self, name):
        self.name = name
        self.weights = defaultdict(float)
        self.discount = 1
        self.epsilon = 0.1
        #self.featureExtractor = identityFeatureExtractor
        self.featureExtractor = featureExtractor
        self.numIters = 0

    # Return the Q function associated with the weights and features
    def getQ(self, state, action):
        score = 0
        for f, v in self.featureExtractor(state, action):
            score += self.weights[f] * v
        return score

    # Call this function to get the step size to update the weights.
    def getStepSize(self):
        return 1.0 / math.sqrt(self.numIters)

    def placeShips(self, board, ships): 
        Util.randomPlaceShips(board, ships)

    def actions(self, state):
        actions = []
        # Randomly select an opponent to attack for now
        opponentToAttack = random.choice(state.getOpponents(self.name))
        targets = state.legalTargets(opponentToAttack)
        torpedos = state.getTorpedos(self.name)
        for torpedo, count in torpedos.iteritems():
            for target in targets:
                actions.append(TorpedoAction(torpedo, target, opponentToAttack))
        return actions

    # This algorithm will produce an action given a state.
    # Here we use the epsilon-greedy algorithm: with probability
    # |epsilon|, take a random action.
    def getAction(self, state):
        self.numIters += 1
        if random.random() < self.epsilon:
            return random.choice(self.actions(state))
        else:
            validActions = [(self.getQ(state, action), action) for action in self.actions(state)]
            bestScore = max(validActions)[0]
            bestActions = [validActions[index] for index in range(len(validActions)) if (validActions[index][0] == bestScore)]
            return random.choice(bestActions)[1]

    def incorporateFeedback(self, state, action, reward, newState):
        v_opt = 0

        if not newState.isEnd():
            v_opt = max(self.getQ(newState, action) for action in self.actions(newState))

        target = reward + self.discount * v_opt
        prediction = self.getQ(state, action)
        update = self.getStepSize() * (prediction - target)

        for f, v in self.featureExtractor(state, action):
            self.weights[f] = self.weights[f] - (update * v)

    def prepareForTesting(self):
        self.epsilon = 0
        print "Learned weights: " 
        print self.weights

