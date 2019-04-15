import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

def plot_population_growth_model():
	pop = 0.1*np.array((range(100)))
	change = np.multiply(4.077*pop, np.exp(-0.8*pop))

	plt.plot(pop, change)
	plt.grid(True)
	plt.xlabel('Current population size (millions of fish)')
	plt.ylabel('New recruits (millions of fish)')
	plt.show()

def plot_policy_vs_value(p_policy, v_policy):
	x = 0.05*np.array(range(len(p_policy)))
	plt.plot(x, 0.05*p_policy, color='#9CBA7F', linewidth=2)
	plt.plot(x, 0.05*v_policy, color='#8A2BE2', linewidth=2)
	plt.xlabel('Population size (millions of fish)')
	plt.ylabel('Policy/Fish to harvest (millions of fish)')
	plt.grid(True)
	plt.legend(['value iteration', 'policy iteration'], loc='lower right')
	plt.show()

def plot_exploration():
	x = np.array(range(0,100000))
	x1 = 0.8*np.ones((100000))
	y = (1 - (1 / (np.log(x+2))))
	y1 = [min(0.00001*x_val, x1_val) for x_val, x1_val in zip(x, x1)]
	plt.plot(x, y1, color='#8A2BE2', linewidth=2)
	plt.ylabel('Probability of greedy approach')
	plt.ylim(0, 1)
	plt.xlabel('Iteration')
	plt.grid(True)
	plt.show()

def plot_q_learning(q_policy):
	x0 = 0.05*np.array(range(len(q_policy)))
	q_policy = [min(x_val, y_val) for x_val, y_val in zip(x0, q_policy)]
	# x1 = 0.01*np.array(range(len(q_policy)))
	plt.plot(x0, q_policy, color='#9CBA7F', linewidth=2)
	plt.xlabel('Population size (millions of fish)')
	plt.ylabel('Policy/Fish to harvest (millions of fish)')
	plt.grid(True)
	plt.show()