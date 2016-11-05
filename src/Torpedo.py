
class Torpedo:

    def __init__(self, torpedoType, targetPosition):
        self.torpedoType = torpedoType
        self.targetPosition = targetPosition

    def getDamagePattern(self):
        raise NotImplemented

