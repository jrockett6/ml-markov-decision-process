import mdp_salmon
from utils import *
import time

def create_model_matrices(dim=200, discount=0.95):
	scale = 10/dim
	transitions = np.zeros((dim, dim, dim))
	reward = np.zeros((dim, dim))
	for k in range(dim):
		for i in range(dim):
			reward[i][k] = scale*min(k, i)
			for j in range(dim):
				expected_next_season_pop = scale*j
				post_harvest_pop = max((i-k)*scale, 0)
				post_season_mean = post_harvest_pop + 4.077*post_harvest_pop * np.exp(-0.8*post_harvest_pop)
				if post_harvest_pop == 0 and j == 0:
					transitions[k][i][j] = 1
				elif post_harvest_pop == 0:
					transitions[k][i][j] = 0
				else:
					prob_next_season_pop = prob(expected_next_season_pop, post_season_mean, 0.2098)
					transitions[k][i][j] = prob_next_season_pop
			tot = sum(transitions[k][i])
			transitions[k][i] = np.array([j/tot for j in transitions[k][i]])

	return transitions, reward, discount

def prob(x, mu, sd):
	const = 1/(2*np.pi*sd**2)**0.5
	exp = np.exp(-(x-mu)**2/(2*sd**2))
	return const*exp

def plot_compare_discount_factors(transitions, reward):
	discount = list(0.1*np.array(range(5))+0.5)
	discount.append(0.99)
	x = 0.05*np.array(range(200))
	colors = ["salmon","dodgerblue", "springgreen", "darkorange", "aqua", "mediumorchid"]
	for i in range(len(discount)):
		value_iteration = mdp_salmon.ValueIteration(transitions, reward, discount[i], epsilon=0.01, max_iter=1000, initial_value=0)		
		value_iteration.run()

		plt.plot(x, 0.05*value_iteration.policy, color=colors[i], linewidth=2)

	plt.xlabel('Population size (millions of fish)')
	plt.ylabel('Policy/Fish to harvest (millions of fish)')
	plt.grid(True)
	legend = ['discount value : {}'.format(disc_val) for disc_val in discount]
	plt.legend(legend, loc='lower right')
	plt.show()

def plot_compare_state_size():
	dim = list(range(100,300,10))
	policy_iterats = []
	value_iterats = []
	for i in range(len(dim)):
		print(i)
		transitions, reward, discount = create_model_matrices(dim=dim[i])
		policy_iteration = mdp_salmon.PolicyIteration(transitions, reward, discount, policy0=None, max_iter=1000, eval_type=1)
		policy_iteration.run()
		policy_iterats.append(policy_iteration.time)

		value_iteration = mdp_salmon.ValueIteration(transitions, reward, discount, epsilon=0.01, max_iter=1000, initial_value=0)
		value_iteration.run()
		value_iterats.append(value_iteration.time)

	plt.plot(dim, value_iterats, color='#9CBA7F', linewidth=2)
	plt.plot(dim, policy_iterats, color='#8A2BE2', linewidth=2)
	plt.xlabel('State space size')
	plt.ylabel('Time to converge (seconds)')
	plt.grid(True)
	plt.legend(['value iteration', 'policy iteration'], loc='lower right')
	plt.show()

# def plot

def main():
	# transitions, reward, discount = create_model_matrices()

	# # Policy iteration
	policy_iteration = mdp_salmon.PolicyIteration(transitions, reward, discount, policy0=None, max_iter=1000, eval_type=1)
	policy_iteration.run()

	# # #Value iteration
	value_iteration = mdp_salmon.ValueIteration(transitions, reward, discount, epsilon=0.01, max_iter=1000, initial_value=0)
	value_iteration.run()

	# #mdp_salmon
	q_learning = mdp_salmon.QLearning(transitions, reward, discount, n_iter=300000000)
	q_learning.run()
	# print(q_learning.time)

	# plot_exploration()
	# plot_q_learning(0.05*np.array(q_learning.policy))
	# plot_policy_vs_value(policy_iteration.policy, value_iteration.policy)
	# plot_compare_discount_factors(transitions, reward)
	# plot_compare_state_size()

if __name__ == '__main__':
	main()

#https://swfsc.noaa.gov/publications/CR/1980/8060.PDF