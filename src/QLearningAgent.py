from collections import defaultdict
from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
import random
import math


def identityFeatureExtractor(state, action):
    featureKey = (state, action)
    featureValue = 1
    return [(featureKey, featureValue)]


def distFeatureExtractor(state, action):
    features = []
    opponentBoard = state.getBoard(action.getTargetAgentName())
    hitRowDist = opponentBoard.getDistNearestSameRowHit(action.getTarget().x, action.getTarget().y)
    missRowDist = opponentBoard.getDistNearestSameRowMiss(action.getTarget().x, action.getTarget().y)
    hitColDist = opponentBoard.getDistNearestSameColHit(action.getTarget().x, action.getTarget().y)
    missColDist = opponentBoard.getDistNearestSameColMiss(action.getTarget().x, action.getTarget().y)
    features.append(('hitRowDist='+str(hitRowDist), 1))
    #features.append(('missRowDist='+str(missRowDist), 1))
    features.append(('hitColDist='+str(hitColDist), 1))
    #features.append(('missColDist='+str(missColDist), 1))
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

    def placeShip(self, ship): 
        raise NotImplementedError()

    def actions(self, state):
        actions = []
        #TODO: Setting 0 only works for 1 opponent
        opponentToAttack = state.getOpponents(self.name)[0]
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
            return max((self.getQ(state, action), action) for action in self.actions(state))[1]

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

