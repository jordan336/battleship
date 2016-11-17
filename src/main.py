
from Game import Game
from ClassicRules import ClassicRules
from MiniGameRules import MiniGameRules
from HumanAgent import HumanAgent

if __name__ == '__main__':

    # Mini game is 5x5 for a quick game, classic game is 10x10
    #rules = ClassicRules
    rules = MiniGameRules
    
    agents = [HumanAgent("Kai", rules)]
    battleshipGame = Game(rules, agents)
    battleshipGame.run()
    #battleshipGame.drawCurrentState()

    
    
    
#####################################################################
# Old test codes below
#####################################################################    
                # TODO move these tests to a unit testing framework?

            # assert(Position(0, 0) == Position(0, 0))
            # assert(Position(0, 1) != Position(1, 0))

            # grid = Grid(10, 10)
            # print "(0, 0)", grid.getValidNeighbors(Position(0, 0))
            # print "(0, 1)", grid.getValidNeighbors(Position(0, 1))
            # print "(1, 0)", grid.getValidNeighbors(Position(1, 0))
            # print "(1, 1)", grid.getValidNeighbors(Position(1, 1))
            
            # carrier = Ship("carrier", Position(1, 1), '0', [1, 1, 1, 1, 1], 10)

            # torpedo = ClassicTorpedo()
            # action = TorpedoAction(ClassicTorpedo(), Position(1, 1))
            # print "(1, 1) damage: ", action.getTorpedo().getDamagePattern(Position(1, 1))
            # print "(1, 0) damage: ", action.getTorpedo().getDamagePattern(Position(1, 0))
            # print "(0, 0) damage: ", action.getTorpedo().getDamagePattern(Position(0, 0))
            # print "----------------------------------"

            # print action.getType()
            # print "(1, 1) damage: ", action.getTorpedo().getDamagePattern(Position(1, 1))
            # print "(1, 0) damage: ", action.getTorpedo().getDamagePattern(Position(1, 0))
            # print "(0, 0) damage: ", action.getTorpedo().getDamagePattern(Position(0, 0))


            # boards = [grid]
            # ships = [carrier]
            # torpedo = []
            # numAgents = 1
            # state = State(boards, ships, torpedo, numAgents)


            # state.generateSuccessor(action) 
            # print "Legal targets remaining:"
            # print state.legalTargets() 
            # TextDisplay.draw(boards[0], ships, showShips=True)