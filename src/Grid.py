
from Position import Position

class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.missed = []
        self.hit = []

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
        
    def getHitPositions(self):
        return self.hit
    
    def getMissedPositions(self):
        return self.missed

    def setHitPosition(self, position):
        self.hit.append(position)
    
    def setMissedPosition(self, position):
        self.missed.append(position)
        
    def queryPosition(self, position):
        if position in self.hit:
            return 'hit'
        elif position in self.missed:
            return 'missed'
        else:
            return 'unknown'
            
    def queryPositionHit(self, position):
        if position in self.hit:
            return True
        else:
            return False

    def queryPositionMissed(self, position):
        if position in self.missed:
            return True
        else:
            return False
        
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


