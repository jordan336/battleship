
from Action import Action

"""
TorpedoAction

Fullfill the Action interface with the type
ACITON_TYPE_FIRE_TORPEDO.
"""
class TorpedoAction(Action):

    def __init__(self, torpedo, target, targetAgentName):
        Action.__init__(self, Action.ACTION_TYPE_FIRE_TORPEDO)
        self.torpedo = torpedo
        self.target = target
        self.targetAgentName = targetAgentName

    def getTorpedo(self):
        return self.torpedo

    def getTarget(self):
        return self.target

    def getTargetAgentName(self):
        return self.targetAgentName

