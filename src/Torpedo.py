from Position import Position

class Torpedo:

    def __init__(self, torpedoType):
        self.torpedoType = torpedoType
        
    def getTorpedoType(self):
        return self.torpedoType

    def getDamage(self, target, position):
        raise NotImplementedError()

