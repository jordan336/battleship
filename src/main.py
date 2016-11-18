
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

