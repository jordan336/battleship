from Position import Position

"""
Grid class

The Grid class represents one Agent's game board.
The Grid contains the dimensions of the board and 
the state of each square, whether it was a hit, miss, or
has not been explored.
"""
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

    def getDistNearestSameRowHit(self, x, y, ignorePositions=[]):
        positions = [pos for pos in self.getHitPositions() if pos not in ignorePositions]
        return self._getDistSameRow(positions, x, y)

    def getDistNearestSameRowMiss(self, x, y, ignorePositions=[]):
        positions = [pos for pos in self.getMissedPositions() if pos not in ignorePositions]
        return self._getDistSameRow(positions, x, y)

    def getDistNearestSameColHit(self, x, y, ignorePositions=[]):
        positions = [pos for pos in self.getHitPositions() if pos not in ignorePositions]
        return self._getDistSameCol(positions, x, y)

    def getDistNearestSameColMiss(self, x, y, ignorePositions=[]):
        positions = [pos for pos in self.getMissedPositions() if pos not in ignorePositions]
        return self._getDistSameCol(positions, x, y)

    def _getDistSameRow(self, positions, x, y):
        posOnSameRow = [pos for pos in positions if pos.y == y]
        if len(posOnSameRow) > 0:
            return min(abs(x - pos.x) for pos in posOnSameRow)
        else:
            return -1

    def _getDistSameCol(self, positions, x, y):
        posOnSameCol = [pos for pos in positions if pos.x == x]
        if len(posOnSameCol) > 0:
            return min(abs(y - pos.y) for pos in posOnSameCol)
        else:
            return -1

    """
    getContinuousVerticalHits()

    Return the number of continuous vertical hits, assuming the 
    given position is also a hit.
    """
    def getContinuousVerticalHits(self, x, y):
        posOnSameCol = [pos for pos in self.getHitPositions() if pos.x == x]
        continuous = [Position(x, y)]
        noChange = False
        while not noChange:
            noChange = True
            for pos in posOnSameCol:
                for continuousPos in continuous:
                    if pos not in continuous and abs(pos.y - continuousPos.y) == 1:
                        continuous.append(pos)
                        noChange = False
        return len(continuous)

    """
    getContinuousHorizontalHits()

    Return the number of continuous horizontal hits, assuming the 
    given position is also a hit.
    """
    def getContinuousHorizontalHits(self, x, y):
        posOnSameRow = [pos for pos in self.getHitPositions() if pos.y == y]
        continuous = [Position(x, y)]
        noChange = False
        while not noChange:
            noChange = True
            for pos in posOnSameRow:
                for continuousPos in continuous:
                    if pos not in continuous and abs(pos.x - continuousPos.x) == 1:
                        continuous.append(pos)
                        noChange = False
        return len(continuous)

    """
    getDownVerticalMissedLength()

    Get the downward vertical length of the continuous unmissed squares containing x, y.
    """
    def getDownVerticalMissedLength(self, x, y):

        if self.queryPosition(Position(x, y)) == 'missed':
            return 0

        gapSquares = [Position(x, y)]

        # Explore downwards in the column
        col = y - 1
        while col >= 0:
            if self.queryPosition(Position(x, col)) != 'missed':            
                gapSquares.append(Position(x, col))
                col -= 1
            else:
                break

        return len(gapSquares)

    """
    getUpVerticalMissedLength()

    Get the upward vertical length of the continuous unmissed squares containing x, y.
    """
    def getUpVerticalMissedLength(self, x, y):

        if self.queryPosition(Position(x, y)) == 'missed':
            return 0

        gapSquares = [Position(x, y)]

        # Explore upwards in the column
        col = y + 1
        while col < self.height:
            if self.queryPosition(Position(x, col)) != 'missed':            
                gapSquares.append(Position(x, col))
                col += 1
            else:
                break

        return len(gapSquares)

    """
    getLeftHorizontalMissedLength()

    Get the leftward horizontal length of the continuous unmissed squares containing x, y.
    """
    def getLeftHorizontalMissedLength(self, x, y):

        if self.queryPosition(Position(x, y)) == 'missed':
            return 0

        gapSquares = [Position(x, y)]

        # Explore leftwards in the row
        row = x - 1
        while row >= 0:
            if self.queryPosition(Position(row, y)) != 'missed':            
                gapSquares.append(Position(row, y))
                row -= 1
            else:
                break

        return len(gapSquares)

    """
    getRightHorizontalMissedLength()

    Get the rightward horizontal length of the continuous unmissed squares containing x, y.
    """
    def getRightHorizontalMissedLength(self, x, y):

        if self.queryPosition(Position(x, y)) == 'missed':
            return 0

        gapSquares = [Position(x, y)]

        # Explore rightwards in the row
        row = x + 1
        while row < self.width:
            if self.queryPosition(Position(row, y)) != 'missed':            
                gapSquares.append(Position(row, y))
                row += 1
            else:
                break

        return len(gapSquares)


