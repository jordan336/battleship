import argparse
from Game import Game
from ClassicRules import ClassicRules
from MiniGameRules import MiniGameRules
from OneShipRules import OneShipRules
from ClassicStationaryRules import ClassicStationaryRules
from HumanAgent import HumanAgent
from RandomAgent import RandomAgent
from HuntAndTargetAgent import HuntAndTargetAgent
from QLearningAgent import QLearningAgent
from NoOpAgent import NoOpAgent
from Statistics import Statistics

if __name__ == '__main__':

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='AI learning agent for the game of Battleship')
    parser.add_argument('-g', '--games', type=int, nargs=1, default=[1], help='Number of games to play')
    parser.add_argument('-t', '--train_iterations', type=int, nargs=1, default=[10], help='Number of training games to play')
    parser.add_argument('-a', '--agents', nargs='+', default=['QLearning'], choices=['Human', 'Random', 'HuntAndTarget', 'QLearning'], help='Agents to play the game')
    parser.add_argument('-n', '--names', nargs='+', default=[], help='Agent names, specified in the same order as -a')
    parser.add_argument('-r', '--rules', nargs=1, default=['Classic'], choices=['Classic', 'Mini', 'OneShip', 'ClassicStationary'], help='Game rules')
    parser.add_argument('-R', '--train_rules', nargs=1, default=['NotSet'], choices=['Classic', 'Mini', 'OneShip'], help='Game rules for training only')
    parser.add_argument('-s', '--stats', action='store_true', default=False, help='Output statistics for each game completed')
    parser.add_argument('-S', '--stats_all', action='store_true', default=False, help='Output statistics when all games are complete')
    parser.add_argument('-c', '--constant_start_state', action='store_true', default=False, help='Always start from the same state')
    args = parser.parse_args()

    # Game iterations
    numTestGamesToPlay = args.games[0]
    numTrainingGamesToPlay = args.train_iterations[0]

    # Test rules
    # Mini game is 5x5 for a quick game, classic game is 10x10
    if args.rules[0] == 'Classic':
        rules = ClassicRules
    elif args.rules[0] == 'OneShip':
        rules = OneShipRules
    elif args.rules[0] == 'ClassicStationary':
        rules = ClassicStationaryRules
    else:
        rules = MiniGameRules

    # Training rules
    if args.train_rules[0] == 'NotSet':
        trainRules = rules
    elif args.train_rules[0] == 'Classic':
        trainRules = ClassicRules
    elif args.train_rules[0] == 'OneShip':
        trainRules = OneShipRules
    else:
        trainRules = MiniGameRules

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

    avgNumMoves = {}
    avgScore = {}
    wins = {}

    # statistics
    if args.stats or args.stats_all:
        stats = Statistics(rules, agents)
        stats.prepareForTraining()
    else:
        stats = None

    # training games
    trainGame = Game(trainRules, agents, stats, args.constant_start_state)
    print '==============================='
    print 'TRAINING GAMES'
    print '==============================='
    for i in range(numTrainingGamesToPlay):
        trainGame.run()
        if stats is not None:
            stats.endGame()

    # Prepare for testing (e.g. set epsilon to 0)
    if stats is not None:
        stats.prepareForTesting()
    for agent in agents:
        agent.prepareForTesting()

    # test games
    testGame = Game(rules, agents, stats, args.constant_start_state)
    print '==============================='
    print 'TEST GAMES'
    print '==============================='
    for i in range(numTestGamesToPlay):
        gameStats = testGame.run()

        # output per game stats
        for agent, (moves, score, win) in gameStats.iteritems():
            print '{:17s}: Win({:d}), Moves ({:3d}), Score({:3d})'.format(agent, win, int(moves), int(score))
            if agent in avgNumMoves:
                avgNumMoves[agent] += moves
                avgScore[agent] += score
                if win:
                    wins[agent] += 1
            else:
                avgNumMoves[agent] = moves
                avgScore[agent] = score
                if win:
                    wins[agent] = 1
                else:
                    wins[agent] = 0
        if stats is not None:
            if args.stats:
                stats.outputStatistics()
            stats.endGame()

    # all test games complete, output cumulative stats
    if numTestGamesToPlay > 0:
        print
        print '==============================='
        print 'Number of test games played:', numTestGamesToPlay
        for agent in avgNumMoves:
            print '{:17s}: Wins ({:03d}), Avg. number of moves taken ({:05.2f}), Avg. score({:06.2f})'.format(agent, wins[agent], (float(avgNumMoves[agent]) / numTestGamesToPlay), (float(avgScore[agent]) / numTestGamesToPlay))
    if stats is not None and args.stats_all:
        stats.outputAllGamesStatistics()

