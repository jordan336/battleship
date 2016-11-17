from Position import Position
from Rules import Rules
from Ship import Ship
from ClassicTorpedo import ClassicTorpedo
from Grid import Grid

class ClassicRules(Rules):

    @staticmethod
    def getBoards():
        # Board dimensions
        return [Grid(10, 10)]

    @staticmethod
    def getShips():
        # Ship positions/orientations will be updated later when placing ships
        carrier = Ship("Carrier", [1, 1, 1, 1, 1], 10)
        battleship = Ship("Battleship", [1, 1, 1, 1], 8)
        cruiser = Ship("Cruiser", [1, 1, 1], 6)
        submarine = Ship("Submarine", [1, 1, 1], 6)
        destroyer = Ship("Destroyer", [1, 1], 4)
        return [carrier, battleship, cruiser, submarine, destroyer]

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

