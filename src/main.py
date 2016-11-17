
from Game import Game
from ClassicRules import ClassicRules
from MiniGameRules import MiniGameRules
from HumanAgent import HumanAgent
from RandomAgent import RandomAgent
from HuntAndTargetAgent import HuntAndTargetAgent

if __name__ == '__main__':

    numGamesToPlay = 10
    avgNumMoves = 0
    avgScore = 0

    # Mini game is 5x5 for a quick game, classic game is 10x10
    rules = ClassicRules
    #rules = MiniGameRules
    
    # Choose the agent to use for the game.
    #agents = [HumanAgent("Kai", rules)]
    #agents = [RandomAgent("Random", rules)]
    agents = [HuntAndTargetAgent("HuntAndTarget", rules)]
    battleshipGame = Game(rules, agents)
    for i in range(numGamesToPlay):
        numMoves, score = battleshipGame.run()
        avgNumMoves += numMoves
        avgScore += score
    print '==============================='
    print 'Number of games played:', numGamesToPlay
    print 'Avg number of moves taken:', (avgNumMoves / numGamesToPlay)
    print 'Avg score:', (avgScore / numGamesToPlay)
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