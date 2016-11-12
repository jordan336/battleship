
from Position import Position
from Grid import Grid
from ClassicTorpedo import ClassicTorpedo
from TorpedoAction import TorpedoAction
from State import State
from Ship import Ship
from TextDisplay import TextDisplay


if __name__ == '__main__':

    # TODO move these tests to a unit testing framework?

    assert(Position(0, 0) == Position(0, 0))
    assert(Position(0, 1) != Position(1, 0))

    grid = Grid(10, 10)
    print "(0, 0)", grid.getValidNeighbors(Position(0, 0))
    print "(0, 1)", grid.getValidNeighbors(Position(0, 1))
    print "(1, 0)", grid.getValidNeighbors(Position(1, 0))
    print "(1, 1)", grid.getValidNeighbors(Position(1, 1))
    
    carrier = Ship("carrier", Position(1, 1), '0', [0, 0, 0, 0, 0], 10)

    torpedo = ClassicTorpedo(Position(1, 1))
    print "(1, 1) damage: ", torpedo.getDamagePattern(Position(1, 1))
    print "(1, 0) damage: ", torpedo.getDamagePattern(Position(1, 0))
    print "(0, 0) damage: ", torpedo.getDamagePattern(Position(0, 0))
    print "----------------------------------"

    action = TorpedoAction(torpedo)
    print action.getType()
    print "(1, 1) damage: ", action.getTorpedo().getDamagePattern(Position(1, 1))
    print "(1, 0) damage: ", action.getTorpedo().getDamagePattern(Position(1, 0))
    print "(0, 0) damage: ", action.getTorpedo().getDamagePattern(Position(0, 0))


    boards = [grid]
    ships = [carrier]
    torpedo = []
    numAgents = 1
    state = State(boards, ships, torpedo, numAgents)


    state.generateSuccessor(action) 
    print "Legal targets remaining:"
    print state.legalTargets() 
    TextDisplay.draw(boards[0], ships, showShips=True)
