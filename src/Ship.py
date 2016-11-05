
class Ship:

    ORIENTATION_0_DEG   = '0'
    ORIENTATION_90_DEG  = '90'
    ORIENTATION_180_DEG = '180'
    ORIENTATION_270_DEG = '270'


    def __init__(self, name, boardPosition, orientation, damageList):
        self.name = name
        self.boardPosition = boardPosition
        self.orientation = orientation
        self.length = len(damageList)
        self.damageList = damageList
        self.sunk = False


    def getPosition(self):
        return self.position


    def getOrientation(self):
        return self.orientation


    def isSunk(self):
        return self.sunk


    def takeDamage(self):
        raise NotImplemented


    def getDamage(self):
        raise NotImplemented

