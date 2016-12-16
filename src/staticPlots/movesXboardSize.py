import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sizes = [100, 121, 144, 169, 196, 225, 289, 400]

random = [95.36, 93.55, 94.29, 94.71, 94.24, 94.81, 95.32, 95.02]
qlearning = [50.28, 49.07, 47.41, 45.48, 46.28, 43.5, 39.03, 38.7]
hunt = [61.78, 59.85, 58.11, 56.45, 53.94, 55.13, 51.4, 52.15]


plt.plot(sizes, random, 'r-o', label='Random')
plt.plot(sizes, hunt, 'g-o', label='HuntAndTarget')
plt.plot(sizes, qlearning, 'b-o', label='QLearning')
plt.xlabel("Num. Board Squares")
plt.ylabel("Percent Squares Explored")
plt.title("Amount of Game Board Explored")
plt.legend(bbox_to_anchor=(1.005, 1), loc=2)
plt.grid(True)
plt.savefig('amountGameBoardExplored', bbox_inches='tight')

