
from Action import Action

"""
TorpedoAction implementing Action interface

The TorpedoAction is an Action that represents
firing a Torpedo at a target location and a
target agent.
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

