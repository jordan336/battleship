Battleship
----------

Stanford University
CS 221 Fall 2016

Jordan Ebel (jebel)
Kai Wan (kaiw)


TODO List
---------
* Improve Q-Learning agent
* Improve this readme
* Move placeShips() logic out of Game
* More unit testing
* State should update torpedo lists when an Agent fires a torpedo
* Agent statistics
* Grid needs to handle case where there is a hit at a position, but the ship still has hit points at that position.
  An Agent should still be allowed to fire at a hit position in this case, or maybe its always allowed?
* Type check user input in HumanAgent
* Scoring systems needs overhaul
    - Remove score from Rules
* Implement a logging system?
* Support more than 2 agents (if desired):
    - In a few places, the Agents expect only having 1 opponent


Run Game
--------
python src/main.py


Run Tests
---------
python test/TestRunner.py


