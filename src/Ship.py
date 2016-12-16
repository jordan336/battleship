from Position import Position

"""
Ship class

The Ship class contains the position, orientation, hit points,
and point value of a ship.  Ships are located on the Grid game
board, with the left most square serving as the ship's position.
Each Ship can be oriented in one of 4 orientations, which are
rotations of the ship around the left most square.

Ships should support being placed, taking damage after being hit
by a torpedo, and reporting the score value based on the damage
the ship has sustained.
"""
class Ship:

    ORIENTATION_0_DEG   = '0'
    ORIENTATION_90_DEG  = '90'
    ORIENTATION_180_DEG = '180'
    ORIENTATION_270_DEG = '270'


    """
    __init__
    
    Create a ship.

    - name:          Unique identifier for the ship

    - damageList:    List of integers representing the damage points remaining.  
                     Each entry in the list represents one segment of the ship.

    - value:         The total value this ship for the opponent if sunk

    - boardPosition: Position representing the first segment of this ship

    - orientation:   Ship orientation, in clockwise degrees

    - immovable:     True if the position is set at creation and the ship cannot later be moved.
    """
    def __init__(self, name, damageList, value, boardPosition=Position(0, 0), orientation='0', immovable=False):
        self.name = name
        self.damageList = damageList
        self.value = value
        self.boardPosition = boardPosition
        self.orientation = orientation
        self.length = len(damageList)
        self.sunk = False
        self.immovable = immovable

    def getName(self):
        return self.name

    def getPosition(self):
        return self.boardPosition

    """
    getPositions

    Get a list of Positions, one for each segment of this ship.
    """
    def getPositions(self):
        positions = []
        for i in range(self.length):
            if self.orientation == self.ORIENTATION_0_DEG:
                positions.append(Position(self.boardPosition.x+i, self.boardPosition.y)) 
            elif self.orientation == self.ORIENTATION_90_DEG:
                positions.append(Position(self.boardPosition.x, self.boardPosition.y+i)) 
            elif self.orientation == self.ORIENTATION_180_DEG:
                positions.append(Position(self.boardPosition.x-i, self.boardPosition.y)) 
            else:
                positions.append(Position(self.boardPosition.x, self.boardPosition.y-i)) 
        return positions

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
            if (position.y == self.boardPosition.y and position.x >= self.boardPosition.x and position.x <= self.boardPosition.x + (self.length - 1)):
                return abs(position.x - self.boardPosition.x)
        elif self.orientation is self.ORIENTATION_90_DEG:
            if (position.x == self.boardPosition.x and position.y >= self.boardPosition.y and position.y <= self.boardPosition.y + (self.length - 1)):
                return abs(position.y - self.boardPosition.y)
        elif self.orientation is self.ORIENTATION_180_DEG:
            if (position.y == self.boardPosition.y and position.x <= self.boardPosition.x and position.x >= self.boardPosition.x - (self.length - 1)):
                return abs(position.x - self.boardPosition.x)
        elif self.orientation is self.ORIENTATION_270_DEG:
            if (position.x == self.boardPosition.x and position.y <= self.boardPosition.y and position.y >= self.boardPosition.y - (self.length - 1)):
                return abs(position.y - self.boardPosition.y)
        return -1
    

    """
    getScore()
    
    Return the number of points earned for the damage done to this ship.
    The score is defined as the percentage of ship segments that are completely
    destroyed times the total ship value.
    """
    def getScore(self):
        amountDamaged = 0.0
        for damage in self.damageList:
            if damage == 0:
                amountDamaged += 1
        return self.value * (amountDamaged / self.length)

    """
    place()
    
    Updates the ship's position and orientation to the values provided.
    """
    def place(self, position, orientation):
        if not self.immovable:
            self.boardPosition = position
            self.orientation = orientation

    """
    takeDamage()

    Update the ship's hit points after sustaining an attack
    at the specified index with the specified damage amount.
    """
    def takeDamage(self, index, damageAmount):
        if index >= 0 and index < len(self.damageList):
            self.damageList[index] -= damageAmount
        if self.damageList[index] < 0:
            self.damageList[index] = 0
        if sum(self.damageList) <= 0:
            self.sunk = True

    """
    takeDamage_Position()

    Update the ship's hit points after sustaining an attack
    at the specified position with the specified damage amount.
    """
    def takeDamage_Position(self, position, damageAmount):
        self.takeDamage(self.shipSegmentIndex(position), damageAmount)

    """
    getDamage()

    Get the sum of the ship's hit points (damage list).
    """
    def getDamage(self):
        return sum(self.damageList)

    """
    getHits()

    Get the number of squares occupied by the ship that contains zero hit points, i.e. squares that have been completely destroyed by torpedos.
    """
    def getHits(self):
        amountDamaged = 0
        for damage in self.damageList:
            if damage == 0:
                amountDamaged += 1
        return amountDamaged

