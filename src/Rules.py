
class Rules:

    def getShips(self):
        raise NotImplemented

    """
        getTorpedos

        Returns list of tuples with torpedo info, with each tuple specifying the torpedo type and number.
        For example: [ClassicTorpedo, 10]
    """
    def getTorpedos(self):
        raise NotImplementedError()

    def getScore(self):
        raise NotImplementedError()

