from Position import Position
from Rules import Rules
from Ship import Ship
from ClassicTorpedo import ClassicTorpedo
from Grid import Grid

"""
OneShipRules implementing Rules interface

Rules with one ship in the middle of a medium size board.
"""
class OneShipRules(Rules):

    @staticmethod
    def getBoard(agent):
        # Board dimensions
        return Grid(10, 7)

    # One immovable ship, right in the middle of the game board
    @staticmethod
    def getShips(agent):
        ship = Ship("OneShip", [1, 1, 1, 1], 100, boardPosition=Position(3, 3), immovable=True)
        return [ship]

    @staticmethod
    def getTorpedos(agent):
        # Use 999 torpedos for now -- basically unlimited number of torpedos
        return { ClassicTorpedo(): 999 }

