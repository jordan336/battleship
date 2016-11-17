from Position import Position

class Torpedo:

    def __init__(self, torpedoType):
        self.torpedoType = torpedoType
        self.targetPosition = Position(0, 0)
        
    def getTorpedoType(self):
        return self.torpedoType

    def getTargetPosition(self):
        return self.targetPosition

    def setTargetPosition(self, position):
        self.targetPosition = position

    def getDamagePattern(self):
        raise NotImplemented

