
from Action import Action

"""
TorpedoAction

Fullfill the Action interface with the type
ACITON_TYPE_FIRE_TORPEDO.
"""
class TorpedoAction(Action):

    def __init__(self, torpedo):
        Action.__init__(self, Action.ACTION_TYPE_FIRE_TORPEDO)
        self.torpedo = torpedo


    def getTorpedo(self):
        return self.torpedo

