from Agent import Agent

"""
Rules interface

The Rules interface provides the methods necessary to 
set up a new game of Battleship.  The Rules includes the 
game boards, amount and type of ships, and amount and type
of torpedos every Agent is allocated.
"""
class Rules:

    """
    getBoard

    Return a game board (Grid) for the given Agent.
    """
    @staticmethod
    def getBoard(agent):
        raise NotImplementedError()

    """
    getShips

    Returns a list of ships for the given Agent.
    """
    @staticmethod
    def getShips(agent):
        raise NotImplementedError()

    """
    getTorpedos

    Returns list of tuples with torpedo info, with each tuple specifying the torpedo type and number.
    For example: [ClassicTorpedo, 10]
    """
    @staticmethod
    def getTorpedos(agent):
        raise NotImplementedError()

