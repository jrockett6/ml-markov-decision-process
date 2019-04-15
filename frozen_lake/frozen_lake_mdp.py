from frozen_lake import *
from utils import *
from mdptoolbox import mdp

def get_environement():
	lake = FrozenLake(5, .2, random_state=15).lake
	transitions = create_transition_matrix(len(lake), 0.8)
	reward = create_reward_matrix(lake)
	discount = .9

	return transitions, reward, discount, lake

def main():
	transitions, reward, discount, lake = get_environement()
	
	#Policy iteration
	policy_iteration = mdp.PolicyIteration(transitions, reward, discount, policy0=None, max_iter=1000, eval_type=0)
	policy_iteration.run()
	print_as_grid(policy_iteration.policy, lake, 5)
	print(policy_iteration.time)
	print(policy_iteration.iter)

	# #Value iteration
	value_iteration = mdp.ValueIteration(transitions, reward, discount, epsilon=0.01, max_iter=1000, initial_value=0)
	value_iteration.run()
	print_as_grid(value_iteration.policy, lake, 5)
	print(value_iteration.time)
	print(value_iteration.iter)

	# #MDP
	q_learning = mdp.QLearning(transitions, reward, discount, n_iter=20000000)
	q_learning.run()
	print_as_grid(q_learning.policy, lake, 5)
	print(q_learning.time)

	# programpause = input("press enter to continue")


if __name__ == '__main__':
	main()