
from Action import Action

"""
TorpedoAction

Fullfill the Action interface with the type
ACITON_TYPE_FIRE_TORPEDO.
"""
class TorpedoAction(Action):

    def __init__(self, torpedo, target):
        Action.__init__(self, Action.ACTION_TYPE_FIRE_TORPEDO, target)
        self.torpedo = torpedo
        self.torpedo.setTargetPosition(target)


    def getTorpedo(self):
        return self.torpedo

