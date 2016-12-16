from Ship import Ship
from State import State
from Action import Action

"""
Agent interface

This interface exposes the functionality required
for an Agent to play Battleship.  Agents should 
implement this interface in order to participate
in a game.
"""
class Agent:

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def placeShips(self, board, ships): 
        raise NotImplementedError()

    def getAction(self, State): 
        raise NotImplementedError()

    def incorporateFeedback(self, state, action, reward, newState):
        raise NotImplementedError()

    def prepareForTesting(self):
        raise NotImplementedError()

