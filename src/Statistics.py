import matplotlib
matplotlib.use('Agg')
from matplotlib.colors import LogNorm
import matplotlib.pyplot as pyplot
from Action import Action
from State import State

class Statistics:

    PREFIX_FILEPATH = ''
    PREFIX_CUMULHITS='hits_'
    PREFIX_CUMULHITSALLGAMES='avgHitsAllGames_'
    PREFIX_HEATMAP = 'heatmap_'
    PREFIX_COMBINED_HEATMAP = 'combinedHeatmap'

    def __init__(self, rules, agents):
        self.testing = False
        self.currentGameNum = 1
        self.agentNames = []
        self.targetCounters = {}
        self.hitCounters = {}
        self.persist_numMovesPerGame = {}
        self.persist_hitCounters = {}
        self.boards = {}
        for agent in agents:
            self.agentNames.append(agent.getName())
            self.targetCounters[agent.getName()] = []
            self.hitCounters[agent.getName()] = []
            self.boards[agent.getName()] = rules.getBoard(agent)
            self.persist_numMovesPerGame[agent.getName()] = []
            maxMoves = self.boards[agent.getName()].getWidth() * self.boards[agent.getName()].getHeight()
            self.persist_hitCounters[agent.getName()] = [0 for i in range(maxMoves)]
        
            
    """
    endGame()

    Store and reset any per game stats.
    """
    def endGame(self):
        if not self.testing:
            return
        self._savePersistentData()
        for agentName in self.agentNames:
            self.targetCounters[agentName] = []
            self.hitCounters[agentName] = []
        self.currentGameNum += 1

    """
    prepareForTraining()

    Prepare the module for receiving training experience.
    """
    def prepareForTraining(self):
        self.testing = False

    """
    prepareForTesting()

    Prepare the module for receiving testing experience.
    """
    def prepareForTesting(self):
        self.testing = True

    """
    logAgentTurn()

    For the given agent, store statistics for the game experience.
    Only log test experience for now.
    """
    def logAgentTurn(self, agentName, oldState, action, reward, newState):
        if not self.testing:
            return
        # For stats purpose, assume just one opponent for now.
        # Need to get this because we are actually recording the number of hits made by the agent on the opponent's game board, not on the agent's board.
        opponentName = newState.getOpponents(agentName)[0]
        self.hitCounters[opponentName].append(newState.getHitCount(agentName) )
        if action is not None:
            if action.getType() == Action.ACTION_TYPE_FIRE_TORPEDO:
                self.targetCounters[agentName].append(action.getTarget())

    """
    _savePersistentData()

    Private method to save the persistent game stats across games.
    """
    def _savePersistentData(self):
        for agentName in self.agentNames:
            maxMoves = self.boards[agentName].getWidth() * self.boards[agentName].getHeight()
            numMoves = len(self.hitCounters[agentName])
            maxHits = max(self.hitCounters[agentName])
            if maxHits < 1:
                maxHits = 1
            # Update number of moves taken in current game
            self.persist_numMovesPerGame[agentName].append(numMoves)
            
            # Update the average number of hits for each move across all games
            xdat = []
            ydat = []
            for i, hitNum in enumerate(self.hitCounters[agentName]):
                xdat.append(i)
                ydat.append((float)(hitNum*100/maxHits))
            if not xdat or not ydat:
                return
            # Fill data lists all the way to 100 moves
            for k in range(maxMoves - len(self.hitCounters[agentName])):
                xdat.append(xdat[-1] +1)
                ydat.append(ydat[-1])
            for i in range(maxMoves):
                self.persist_hitCounters[agentName][i] = (float)(self.persist_hitCounters[agentName][i]*(self.currentGameNum - 1.0) + ydat[i])/(self.currentGameNum)

        
    """
    outputStatistics()

    Outputs stats, graphs, plots, files, etc.
    """
    def outputStatistics(self):   
        self._outputHeatmaps()
        self._outputCombinedHeatmap()
        self._outputCumulativeHitCounts()

    """
    _outputCumulativeHitCounts()

    Private method to output a cumulative plot of the number of hits over number of moves. This is a way to show how efficiently an agent plays.
    """
    def _outputCumulativeHitCounts(self):
        pyplot.close('all')
        for agentName in self.agentNames:
            maxMoves = self.boards[agentName].getWidth() * self.boards[agentName].getHeight()
            xdat = []
            ydat = []
            for i, hitNum in enumerate(self.hitCounters[agentName]):
                xdat.append(i)
                ydat.append(hitNum)
            if not xdat or not ydat:
                return
            # Fill data lists all the way to 100 moves
            for k in range(maxMoves - len(self.hitCounters[agentName])):
                xdat.append(xdat[-1] +1)
                ydat.append(ydat[-1])       
            pyplot.plot(xdat, ydat)
            pyplot.xlabel('Num. Moves')
            pyplot.ylabel('Num. Hits')
            pyplot.title('Single game perfromance of agent ' + agentName)
            pyplot.grid(True)
            pyplot.savefig(self.PREFIX_FILEPATH+self.PREFIX_CUMULHITS+'Game-'+str(self.currentGameNum)+'_'+agentName, bbox_inches='tight')
        
    """
    _outputHeatmaps()

    Private method to output the heatmap of Agent moves.
    """
    def _outputHeatmaps(self):
        pyplot.close('all')
        figureCount = 0
        for agentName in self.agentNames:
            agentBoard = self.boards[agentName]
            width = agentBoard.getWidth()
            height = agentBoard.getHeight()
            targets_x = [t.x for t in self.targetCounters[agentName]]
            targets_y = [t.y for t in self.targetCounters[agentName]]
            pyplot.figure(figureCount, figsize=(9, 6))
            pyplot.hist2d(targets_x, targets_y, bins=[width, height], range=[[0, width-1],[0, height-1]])
            pyplot.colorbar()
            pyplot.savefig(self.PREFIX_FILEPATH+self.PREFIX_HEATMAP+'Game-'+str(self.currentGameNum)+'_'+agentName, bbox_inches='tight')
            figureCount += 1

    """
    _outputCombinedHeatmap()

    Private method to output the combined heatmap of all Agent moves.
    """
    def _outputCombinedHeatmap(self):
        names = ''
        pyplot.close('all')
        figure, axes = pyplot.subplots(len(self.agentNames), sharex=True)

        for index, agentName in enumerate(self.agentNames):
            names += agentName + '_'
            agentBoard = self.boards[agentName]
            width = agentBoard.getWidth()
            height = agentBoard.getHeight()
            targets_x = [t.x for t in self.targetCounters[agentName]]
            targets_y = [t.y for t in self.targetCounters[agentName]]
            hist, xbins, ybins, im = axes[index].hist2d(targets_x, targets_y, bins=[width, height], range=[[0, width-1],[0, height-1]])

        figure.set_size_inches(9, 8.5)
        figure.colorbar(im, ax=axes.ravel().tolist())
        figure.savefig(self.PREFIX_FILEPATH+self.PREFIX_COMBINED_HEATMAP+'_'+'Game-'+str(self.currentGameNum)+'_'+names, bbox_inches='tight')

        
    """
    outputAllGamesStatistics()

    Outputs the persistent stats, graphs, plots, files, etc. for all the games that have been played
    """
    def outputAllGamesStatistics(self):
        self._outputAllGamesHitCounts()
        
        
    """
    _outputAllGamesHitCounts()

    Private method to output a cumulative plot of the average number of hits over each move across all games played. This is a way to show how efficiently an agent plays.
    """
    def _outputAllGamesHitCounts(self):
        pyplot.close('all')
        for agentName in self.agentNames:
            maxMoves = self.boards[agentName].getWidth() * self.boards[agentName].getHeight()
            xdat = []
            ydat = self.persist_hitCounters[agentName]
            for i in range(maxMoves):
                xdat.append(i)
            #for i in range(maxMoves):
            #    print "cumul:", xdat[i], ydat[i]
            pyplot.plot(xdat, ydat)
            pyplot.xlabel('Num. Moves')
            pyplot.ylabel('Cumulative percentage of hitpoints acquired')
            pyplot.title('Average performance of agent ' + agentName)
            pyplot.grid(True)
            pyplot.savefig(self.PREFIX_FILEPATH+self.PREFIX_CUMULHITSALLGAMES+'_'+agentName, bbox_inches='tight')
            