
from Position import Position

class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getValidNeighbors(self, position):
        neighbors = []

        # North
        if position.y+1 < self.height:
            neighbors.append(Position(position.x, position.y+1)) 

        # East
        if position.x+1 < self.width:
            neighbors.append(Position(position.x+1, position.y)) 

        # South
        if position.y-1 >= 0:
            neighbors.append(Position(position.x, position.y-1)) 

        # West
        if position.x-1 >= 0:
            neighbors.append(Position(position.x-1, position.y)) 

        return neighbors


