Battleship
----------

Stanford University
CS 221 Fall 2016

Jordan Ebel (jebel)
Kai Wan (kaiw)


TODO List
---------
* Q-Learning agent
* Improve this readme
* Ship.takeDamage() should not assume damage of 1, it should be based on the torpedo
* Move placeShips() logic out of Game
* More unit testing
* Agents should use State to get their list of torpedos, not Rules
* State should update torpedo lists when an Agent fires a torpedo
* Running the tests doesn't work unless ran from battleship/ directory
* Agent statistics
* Need a way for Agents to extract information about other Agents from State.  Right now they need to use
    agent index and there is no mapping of agent index -> Agent.  As a result, agent index is hardcoded to
    0 in a lot of places.


Run Game
--------
python src/main.py


Run Tests
---------
python test/TestRunner.py


