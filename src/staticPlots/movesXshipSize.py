import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sizes = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]

random = [86.8, 91.38, 94.88, 96.36, 97.36, 97.72, 98, 98.36, 98.62, 99]
qlearning = [83.44, 52.76, 49.88, 52.46, 57.34, 65.42, 71.72, 82.3, 90.36, 97.94]
hunt = [84.68, 66.7, 60.48, 62.22, 58.46, 64.86, 67.98, 73.02, 79.18, 83.42]


plt.plot(sizes, random, 'r-o', label='Random')
plt.plot(sizes, hunt, 'g-o', label='HuntAndTarget')
plt.plot(sizes, qlearning, 'b-o', label='QLearning')
plt.xlabel("Ship Size / Board Dimension")
plt.ylabel("Percent Squares Explored")
plt.title("Amount of Game Board Explored As Ship Size Changes")
plt.legend(bbox_to_anchor=(1.005, 1), loc=2)
plt.grid(True)
plt.savefig('amountGameBoardExploredShipSize', bbox_inches='tight')

