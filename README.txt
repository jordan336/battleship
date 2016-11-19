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
* Agents should use State to get their list of torpedos, not Rules
* State should update torpedo lists when an Agent fires a torpedo
* Agent statistics
* Need a way for Agents to extract information about other Agents from State.  Right now they need to use
    agent index and there is no mapping of agent index -> Agent.  As a result, agent index is hardcoded to
    0 in a lot of places.
* Grid needs to handle case where there is a hit at a position, but the ship still has hit points at that position.
  An Agent should still be allowed to fire at a hit position in this case, or maybe its always allowed?


Run Game
--------
python src/main.py


Run Tests
---------
python test/TestRunner.py


