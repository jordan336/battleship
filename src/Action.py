
"""
Action - interface

The Action interface contains common functions representing 
a move in a game of Battleship.  Classic Battleship has one 
action, fire torpedo.  Extensions to the game may provide actions
that allow for moving ships, firing other weapons, defensive 
actions, etc.

Each Action has a type.  If the Action's type is "fireTorpedo", call 
getTorpedo to get the fired torpedo.  Implementing classes for firing 
torpedos should implement getTorpedo, and leave other Action methods 
unimplemented.  It is up to the caller to first check the type of
an Action, then call only the supported methods for that type.
"""
class Action:

    ACTION_TYPE_FIRE_TORPEDO = "fireTorpedo" 

    def __init__(self, type):
        self.actionType = type

    def getType(self):
        return self.actionType
        
    #######################################
    # TorpedoAction methods

    def getTorpedo(self):
        raise NotImplementedError()

    def getTarget(self):
        raise NotImplementedError()

    def getTargetAgentName(self):
        raise NotImplementedError()

    #######################################

