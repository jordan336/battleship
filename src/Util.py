from Position import Position
from Ship import Ship
import random

"""
randomPlaceShips()

Given a game board and list of ships, place the ships on the game board randomly and assign each ship with corresponding positions and orientations. 
"""
def randomPlaceShips(board, ships):
    placedShips = []
    for ship in ships:
        fits = False
        while not fits:
            tryPos = Position(random.randint(0, board.getWidth() - 1), random.randint(0, board.getHeight() - 1))
            orientations = [Ship.ORIENTATION_0_DEG, Ship.ORIENTATION_90_DEG, Ship.ORIENTATION_180_DEG, Ship.ORIENTATION_270_DEG,]
            random.shuffle(orientations)
            for orientation in orientations:
                if shipFits(board, placedShips, ship.getLength(), tryPos, orientation):
                    ship.place(tryPos, orientation)
                    placedShips.append(ship)
                    fits = True

"""
shipFits()

Used by placeShips() to determine whether the ship with given length and position/orientation will fit on the game board. Return false if the ship will overlap with an existing ship that has already been placed, or falls out of the board's range. 
"""                        
def shipFits(board, placedShips, length, headPosition, orientation):
    (x, y) = headPosition.getPosition()
    for i in range(length):
        if (x < 0) or (y < 0) or (x > board.getWidth() -1) or (y > board.getHeight() -1):
            return False
        for placedShip in placedShips:
            if placedShip.hasShip(Position(x, y)):
                return False
        if orientation == Ship.ORIENTATION_0_DEG:
            x += 1
        elif orientation == Ship.ORIENTATION_90_DEG:
            y += 1
        elif orientation == Ship.ORIENTATION_180_DEG:
            x -= 1
        else:
            y -= 1
    return True
    
"""
percentUnhitShipsFit()

Return the percentage of ship configurations that fit in the given
unexplored vertical and horizontal regions.  Only consider ships
that have not been hit yet.
"""
def percentageUnhitShipsFit(ships, rightHorUnexploredLen, leftHorUnexploredLen, upVerUnexploredLen, downVerUnexploredLen):

    total = 0
    fits = 0

    for ship in ships:

        # if the ship has not been hit yet
        if ship.getHits() == 0:

            # each ship can be oriented 0, 90, 180, or 270 degrees
            total += 4

            # check if ship fits, 0 degree
            if ship.getLength() <= rightHorUnexploredLen:
                fits += 1

            # check if ship fits, 90 degree
            if ship.getLength() <= upVerUnexploredLen:
                fits += 1

            # check if ship fits, 180 degree
            if ship.getLength() <= leftHorUnexploredLen:
                fits += 1

            # check if ship fits, 270 degree
            if ship.getLength() <= downVerUnexploredLen:
                fits += 1

    # return percentage of ship orientations that fit in the unexplored regions
    if total > 0:
        return float(fits) / total
    return 1



