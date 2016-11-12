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
    def __init__(self, name, boardPosition, orientation, damageList, value):
        self.name = name
        self.boardPosition = boardPosition
        self.orientation = orientation
        self.length = len(damageList)
        self.damageList = damageList
        self.value = value
        self.sunk = False


    def getPosition(self):
        return self.position


    def getOrientation(self):
        return self.orientation


    def isSunk(self):
        return self.sunk

    """
    hasShip()
    
    Returns true if the ship occupies the square denoted by the given position.
    """    
    def hasShip(self, position):
        if self.orientation is self.ORIENTATION_0_DEG:
            return (position.y == self.boardPosition.y and position.x >= self.boardPosition.x and position.x <= self.boardPosition.x + self.length - 1)
        elif self.orientation is self.ORIENTATION_90_DEG:
            return (position.x == self.boardPosition.x and position.y >= self.boardPosition.y and position.y <= self.boardPosition.y + self.length - 1)
        elif self.orientation is self.ORIENTATION_180_DEG:
            return (position.y == self.boardPosition.y and position.x <= self.boardPosition.x and position.x >= self.boardPosition.x - self.length - 1)
        elif self.orientation is self.ORIENTATION_270_DEG:
            return (position.x == self.boardPosition.x and position.y <= self.boardPosition.y and position.y >= self.boardPosition.y - self.length - 1)
    

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


    def takeDamage(self):
        raise NotImplemented


    def getDamage(self):
        raise NotImplemented

