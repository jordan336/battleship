from Position import Position

class Ship:

    ORIENTATION_0_DEG   = '0'
    ORIENTATION_90_DEG  = '90'
    ORIENTATION_180_DEG = '180'
    ORIENTATION_270_DEG = '270'


    """
    __init__
    
    Create a ship.

    - name:          Unique identifier for the ship

    - boardPosition: Position representing the first segment of this ship

    - orientation:   Ship orientation, in clockwise degrees

    - damageList:    List of integers representing the damage points remaining.  
                     Each entry in the list represents one segment of the ship.

    - value:         The total value this ship for the opponent if sunk
    """
    def __init__(self, name, damageList, value, boardPosition=Position(0, 0), orientation='0'):
        self.name = name
        self.boardPosition = boardPosition
        self.orientation = orientation
        self.length = len(damageList)
        self.damageList = damageList
        self.value = value
        self.sunk = False

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position

    def getLength(self):
        return self.length

    def getOrientation(self):
        return self.orientation


    def isSunk(self):
        return self.sunk

    """
    hasShip()
    
    Returns true if the ship occupies the square denoted by the given position. Returns false otherwise
    
    Use shipSegmentIndex() for a more informative version that provides the relative index of the ship instead of simple True/False.
    """    
    def hasShip(self, position):
        if self.orientation is self.ORIENTATION_0_DEG:
            return (position.y == self.boardPosition.y and position.x >= self.boardPosition.x and position.x <= self.boardPosition.x + (self.length - 1))
        elif self.orientation is self.ORIENTATION_90_DEG:
            return (position.x == self.boardPosition.x and position.y >= self.boardPosition.y and position.y <= self.boardPosition.y + (self.length - 1))
        elif self.orientation is self.ORIENTATION_180_DEG:
            return (position.y == self.boardPosition.y and position.x <= self.boardPosition.x and position.x >= self.boardPosition.x - (self.length - 1))
        elif self.orientation is self.ORIENTATION_270_DEG:
            return (position.x == self.boardPosition.x and position.y <= self.boardPosition.y and position.y >= self.boardPosition.y - (self.length - 1))
    
    """
    shipSegmentIndex()
    
    Returns the relative segment index of the ship that corresponds to the given position. If the given position is not occupied by the ship, returns -1.
    
    For example, assume we have a ship of length 5 starting at position (1, 1) with 90 deg orientation. If we strike at position (1, 3), we will return index of 2. If we strike at position (2, 2) we miss and return index of -1.
    """    
    def shipSegmentIndex(self, position):
        if self.orientation is self.ORIENTATION_0_DEG:
            if (position.y == self.boardPosition.y and position.x >= self.boardPosition.x and position.x <= self.boardPosition.x + self.length - 1):
                return abs(position.x - self.boardPosition.x)
        elif self.orientation is self.ORIENTATION_90_DEG:
            if (position.x == self.boardPosition.x and position.y >= self.boardPosition.y and position.y <= self.boardPosition.y + self.length - 1):
                return abs(position.y - self.boardPosition.y)
        elif self.orientation is self.ORIENTATION_180_DEG:
            if (position.y == self.boardPosition.y and position.x <= self.boardPosition.x and position.x >= self.boardPosition.x - self.length - 1):
                return abs(position.x - self.boardPosition.x)
        elif self.orientation is self.ORIENTATION_270_DEG:
            if (position.x == self.boardPosition.x and position.y <= self.boardPosition.y and position.y >= self.boardPosition.y - self.length - 1):
                return abs(position.y - self.boardPosition.y)
        return -1
    

    """
    getScore()
    
    Return the number of points earned for the damage done to this ship.
    The score is defined as the percentage of ship segments that are completely
    destroyed times the total ship value.

    TODO: support more sophisticated score functions?
    """
    def getScore(self):
        amountDamaged = 0.0
        for damage in damageList:
            if damage == 0:
                amountDamaged += 1
        return self.value * (amountDamaged / self.length)

    """
    place()
    
    Updates the ship's position and orientation to the values provided.
    
    """
    def place(self, position, orientation):
        self.boardPosition = position
        self.orientation = orientation

    def takeDamage(self, index):
        if index >= 0 and index < len(self.damageList):
            self.damageList[index] -= 1
        if sum(self.damageList) == 0:
            self.sunk = True


    def getDamage(self):
        return sum(self.damageList)

