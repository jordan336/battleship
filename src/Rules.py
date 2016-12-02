from Agent import Agent

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

