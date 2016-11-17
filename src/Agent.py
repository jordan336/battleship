
from Ship import Ship
from State import State

class Agent:

    def __init__(self, name):
        self.name = name

    def placeShip(self, Ship): 
        raise NotImplemented

    def getAction(self, State): 
        raise NotImplemented

