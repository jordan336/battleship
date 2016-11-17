from Position import Position
from Rules import Rules
from Ship import Ship
from ClassicTorpedo import ClassicTorpedo
from Grid import Grid

class MiniGameRules(Rules):

    @staticmethod
    def getBoards():
        # Board dimensions
        return [Grid(5, 5)]

    @staticmethod
    def getShips():
        # Ship positions/orientations will be updated later when placing ships
        destroyer = Ship("Destroyer", Position(0, 0), '0', [1, 1], 4)
        return [destroyer]

    """
        getTorpedos

        Returns list of tuples with torpedo info, with each tuple specifying the torpedo type and number.
    """
    @staticmethod
    def getTorpedos():
        # Use 999 torpedos for now -- basically unlimited number of torpedos
        return [(ClassicTorpedo(), 999)]

    @staticmethod
    def getScore():
        # TODO
        return 0
