from Torpedo import Torpedo

"""
ClassicTorpedo implementing Torpedo interface

A classic Battleship torpedo, it does 1 hitpoint
worth of damage on the single square it was 
shot at.
"""
class ClassicTorpedo(Torpedo):
    
    TORPEDO_TYPE_CLASSIC = "classic"

    def __init__(self):
        Torpedo.__init__(self, ClassicTorpedo.TORPEDO_TYPE_CLASSIC)

    def getDamage(self, target, position):
        if (position == target):
            return 1
        else:
            return 0
        
