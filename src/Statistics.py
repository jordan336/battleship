import matplotlib
matplotlib.use('Agg')
from matplotlib.colors import LogNorm
import matplotlib.pyplot as pyplot
from Action import Action
from State import State

class Statistics:

    PREFIX_HEATMAP = 'heatmap_'
    PREFIX_COMBINED_HEATMAP = 'combinedHeatmap'

    def __init__(self, rules, agents):
        self.testing = False
        self.agentNames = []
        self.targetCounters = {}
        self.boards = {}
        for agent in agents:
            self.agentNames.append(agent.getName())
            self.targetCounters[agent.getName()] = []
            self.boards[agent.getName()] = rules.getBoard(agent)

    """
    endGame()

    Store and reset any per game stats.
    """
    def endGame(self):
        # TODO
        pass

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
        if action is not None:
            if action.getType() == Action.ACTION_TYPE_FIRE_TORPEDO:
                self.targetCounters[agentName].append(action.getTarget())

    """
    outputStatistics()

    Outputs stats, graphs, plots, files, etc.
    """
    def outputStatistics(self):
        self._outputHeatmaps()
        self._outputCombinedHeatmap()

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
            pyplot.savefig(self.PREFIX_HEATMAP+agentName, bbox_inches='tight')
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
        figure.savefig(self.PREFIX_COMBINED_HEATMAP+'_'+names, bbox_inches='tight')

