
class Torpedo:

    def __init__(self, torpedoType, targetPosition):
        self.torpedoType = torpedoType
        self.targetPosition = targetPosition


    def getTargetPosition(self):
        return self.targetPosition


    def getDamagePattern(self):
        raise NotImplemented

