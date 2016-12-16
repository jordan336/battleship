
"""
Position class

This class stores the X and Y coordinates of
one square on the game board.
"""
class Position:

    def __init__(self, xPosition, yPosition):
        self.x = xPosition
        self.y = yPosition

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        if isinstance(other, Position):
            return (other.x == self.x) and (other.y == self.y)
        return NotImplemented

    def getPosition(self):
        return (self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))

