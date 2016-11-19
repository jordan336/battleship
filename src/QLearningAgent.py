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


class QLearningAgent(Agent):

    def __init__(self, name):
        self.name = name
        self.weights = defaultdict(float)
        self.discount = 1
        self.epsilon = 0.1
        self.featureExtractor = identityFeatureExtractor
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
        targets = state.legalTargets()
        torpedos = state.getTorpedos()[0]  # TODO Do not hardcode 0
        for torpedo in torpedos:
            for target in targets:
                actions.append(TorpedoAction(torpedo[0], target, 0))
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

