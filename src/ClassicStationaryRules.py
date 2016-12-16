from Position import Position
from Rules import Rules
from Ship import Ship
from ClassicTorpedo import ClassicTorpedo
from Grid import Grid

"""
ClassicStationaryRules

Classic rules, but the ships cannot be moved after initial placement.
"""
class ClassicStationaryRules(Rules):

    @staticmethod
    def getBoard(agent):
        # Board dimensions
        return Grid(10, 10)

    # Classic ships, all immovable, for testing
    @staticmethod
    def getShips(agent):
        carrier = Ship("Carrier", [1, 1, 1, 1, 1], 100, Position(2, 3), Ship.ORIENTATION_90_DEG, immovable=True)
        battleship = Ship("Battleship", [1, 1, 1, 1], 80, Position(0, 0), Ship.ORIENTATION_0_DEG, immovable=True)
        cruiser = Ship("Cruiser", [1, 1, 1], 60, Position(6, 2), Ship.ORIENTATION_180_DEG, immovable=True)
        submarine = Ship("Submarine", [1, 1, 1], 60, Position(8, 1), Ship.ORIENTATION_90_DEG, immovable=True)
        destroyer = Ship("Destroyer", [1, 1], 40, Position(6, 6), Ship.ORIENTATION_0_DEG, immovable=True)
        return [carrier, battleship, cruiser, submarine, destroyer]

    @staticmethod
    def getTorpedos(agent):
        # Use 999 torpedos for now -- basically unlimited number of torpedos
        return { ClassicTorpedo(): 999 }

