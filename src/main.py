
from Position import Position
from Grid import Grid
from ClassicTorpedo import ClassicTorpedo


if __name__ == '__main__':

    assert(Position(0, 0) == Position(0, 0))
    assert(Position(0, 1) != Position(1, 0))

    grid = Grid(10, 10)
    print "(0, 0)", grid.getValidNeighbors(Position(0, 0))
    print "(0, 1)", grid.getValidNeighbors(Position(0, 1))
    print "(1, 0)", grid.getValidNeighbors(Position(1, 0))
    print "(1, 1)", grid.getValidNeighbors(Position(1, 1))

    torpedo = ClassicTorpedo(Position(1, 1))
    print "(1, 1) damage: ", torpedo.getDamagePattern(Position(1, 1))
    print "(1, 0) damage: ", torpedo.getDamagePattern(Position(1, 0))
    print "(0, 0) damage: ", torpedo.getDamagePattern(Position(0, 0))

