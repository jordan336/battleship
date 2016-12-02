import argparse
from Game import Game
from ClassicRules import ClassicRules
from MiniGameRules import MiniGameRules
from HumanAgent import HumanAgent
from RandomAgent import RandomAgent
from HuntAndTargetAgent import HuntAndTargetAgent
from QLearningAgent import QLearningAgent
from NoOpAgent import NoOpAgent

if __name__ == '__main__':

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Battleship game')
    parser.add_argument('-i', '--iterations', type=int, nargs=1, default=[10], help='Number of game iterations to perform')
    parser.add_argument('-a', '--agents', nargs='+', default=['QLearning'], choices=['Human', 'Random', 'HuntAndTarget', 'QLearning'], help='Agents to play the game')
    parser.add_argument('-n', '--names', nargs='+', default=[], help='Agent names, specified in the same order as -a')
    parser.add_argument('-r', '--rules', nargs=1, default=['Classic'], choices=['Classic', 'Mini'], help='Game rules')
    args = parser.parse_args()

    # Game iterations
    numGamesToPlay = args.iterations[0]

    # Mini game is 5x5 for a quick game, classic game is 10x10
    if args.rules[0] == 'Classic':
        rules = ClassicRules
    else:
        rules = MiniGameRules

    # Choose the agents to use for the game.
    agents = []
    for index, agent in enumerate(args.agents):
        if agent == 'Human':
            if index < len(args.names):
                agents.append(HumanAgent(args.names[index]))
            else:
                agents.append(HumanAgent('Human'+str(index)))
        elif agent == 'Random':
            if index < len(args.names):
                agents.append(RandomAgent(args.names[index]))
            else:
                agents.append(RandomAgent('Random'+str(index)))
        elif agent == 'HuntAndTarget':
            if index < len(args.names):
                agents.append(HuntAndTargetAgent(args.names[index]))
            else:
                agents.append(HuntAndTargetAgent('Hunt'+str()))
        else:
            if index < len(args.names):
                agents.append(QLearningAgent(args.names[index]))
            else:
                agents.append(QLearningAgent('QLearningAgent'))

    # Game must be played with at least 2 Agents.  Add an Agent
    # that does nothing if only 1 Agent is given.
    count = 0
    while len(agents) < 2:
        agents.append(NoOpAgent('NoOp'+str(count)))
        count += 1

    avgNumMoves = 0
    avgScore = 0

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

