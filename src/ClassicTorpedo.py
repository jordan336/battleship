from Torpedo import Torpedo

class ClassicTorpedo(Torpedo):
    
    TORPEDO_TYPE_CLASSIC = "classic"

    def __init__(self):
        Torpedo.__init__(self, ClassicTorpedo.TORPEDO_TYPE_CLASSIC)

    def getDamage(self, position):
        if (position == self.targetPosition):
            return 1
        else:
            return 0
        
