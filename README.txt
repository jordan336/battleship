AI Learning Agent for the Game of Battleship

--------------------------------------------

Stanford University
CS 221 Fall 2016

Jordan Ebel (jebel)
Kai Yee Wan (kaiw)

--------------------------------------------

This project contains a programmatic model for the game of Battleship, 
a mechanism for agents to play the game, and a number of agents, 
rules, and game boards.

The Python source is in battleship/src, tests are in battleship/test, 
and documentation is in battleship/doc.  Statistics will be written to
battleship/stats/, which will be created if it does not exist.  Statistics
include plots, heatmaps, and textual game records.

--------------------------------------------

usage: main.py [-h] [-g GAMES] [-t TRAIN_ITERATIONS]
               [-a {Human,Random,HuntAndTarget,QLearning} [{Human,Random,HuntAndTarget,QLearning} ...]]
               [-n NAMES [NAMES ...]]
               [-r {Classic,Mini,OneShip,ClassicStationary}]
               [-R {Classic,Mini,OneShip}] [-s] [-S] [-c]

AI learning agent for the game of Battleship

optional arguments:
  -h, --help            show this help message and exit
  -g GAMES, --games GAMES
                        Number of games to play
  -t TRAIN_ITERATIONS, --train_iterations TRAIN_ITERATIONS
                        Number of training games to play
  -a {Human,Random,HuntAndTarget,QLearning} [{Human,Random,HuntAndTarget,QLearning} ...], --agents {Human,Random,HuntAndTarget,QLearning} [{Human,Random,HuntAndTarget,QLearning} ...]
                        Agents to play the game
  -n NAMES [NAMES ...], --names NAMES [NAMES ...]
                        Agent names, specified in the same order as -a
  -r {Classic,Mini,OneShip,ClassicStationary}, --rules {Classic,Mini,OneShip,ClassicStationary}
                        Game rules
  -R {Classic,Mini,OneShip}, --train_rules {Classic,Mini,OneShip}
                        Game rules for training only
  -s, --stats           Output statistics for each game completed
  -S, --stats_all       Output statistics when all games are complete
  -c, --constant_start_state
                        Always start from the same state

--------------------------------------------

Examples:
    
    python src/main.py
        Play 10 training games and 1 test game with the QLearning agent.

    python src/main.py -g 50 -t 100 QLearning -s -S
        Play 100 training games and 50 test games with the QLearning agent vs. a do-nothing agent (NoOp Agent).  Output per game stats, and cumulative all-game stats.

    python src/main.py -g 50 -t 100 -a QLearning -r ClassicStationary
        Train QLearning agent with 100 games, then play 50 test games using the ClassicStationary rules.

    python src/main.py -g 10 -t 0 -a HuntAndTarget Human Random Random
        Play 10 test games with 1 HuntAndTarget, 1 Human, and 2 Random agents competing.

    python src/main.py -g 1 -t 0 -a QLearning Human -n John_QLearning Joe_Human
        Play 1 test game with a QLearning agent (named John_QLearning) vs. a Human agent (named Joe_Human).

    python src/main.py -g 1 -t 1 Random -r Classic -R Mini -c
        Play 1 training and 1 test game with the Random agent.  Training using Mini rules, play using Classic rules.  Use the same start state for all games.

    python test/TestRunner.py
        Run the unit tests.

--------------------------------------------

Agents:

    - Human          : Ask the human user for targets
    - Random         : Randomly pick targets
    - HuntAndTarget  : Randomly hunt, selectively target neighboring squares
    - QLearning      : Reinforcement learning implementation


Rules:

    - Mini              : Very small board, one ship
    - Classic           : Standard 10x10 board, 5 ships, unlimited torpedos
    - OneShip           : Medium size board, 1 ship in the middle
    - ClassicStationary : Standard board, 5 immovable ships

