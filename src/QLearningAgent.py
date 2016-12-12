from collections import defaultdict
from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
import random
import math
import Util


#TODO remove
from TextDisplay import TextDisplay

def identityFeatureExtractor(state, action):
    featureKey = (state, action)
    featureValue = 1
    return [(featureKey, featureValue)]


def distFeatureExtractor(state, action):
    features = []
    targetX = action.getTarget().x
    targetY = action.getTarget().y
    opponentBoard = state.getBoard(action.getTargetAgentName())
    hitRowDist = opponentBoard.getDistNearestSameRowHit(targetX, targetY)
    missRowDist = opponentBoard.getDistNearestSameRowMiss(targetX, targetY)
    hitColDist = opponentBoard.getDistNearestSameColHit(targetX, targetY)
    missColDist = opponentBoard.getDistNearestSameColMiss(targetX, targetY)
    continuousVerticalHits = opponentBoard.getContinuousVerticalHits(targetX, targetY)
    continuousHorizontalHits = opponentBoard.getContinuousHorizontalHits(targetX, targetY)
    maxContiguousHits = max(continuousVerticalHits, continuousHorizontalHits)

    # exclude feature when there are no hits on the row
    if hitRowDist != -1:
        features.append(('hitRowDist='+str(hitRowDist), 1))

    # exclude feature when there are no hits on the column
    if hitColDist != -1:
        features.append(('hitColDist='+str(hitColDist), 1))

    # missing distances are killing performance, not fully understood why yet
    #features.append(('missRowDist='+str(missRowDist), 1))
    #features.append(('missColDist='+str(missColDist), 1))

    # continuous hits
    # disable for now until more testing
    #if maxContiguousHits != 1:
        #features.append(('contiguousHits='+str(maxContiguousHits), 1))

    return features

class QLearningAgent(Agent):

    def __init__(self, name):
        self.name = name
        self.weights = defaultdict(float)
        self.discount = 1
        self.epsilon = 0.1
        #self.featureExtractor = identityFeatureExtractor
        self.featureExtractor = distFeatureExtractor
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

        # TODO remove
        if self.epsilon == 0:
            opp = state.getOpponents(self.name)[0]
            #TextDisplay.draw(state.getBoard(opp), state.getShips(opp), True) 

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

