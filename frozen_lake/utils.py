import numpy as np


def create_transition_matrix(size, move_prob):
	n_states = size*size
	actions = [(0, -1), (-1, 0), (0, 1), (1, 0)] #L, U, R, D
	transitions = np.zeros((4, n_states, n_states))
	for k in range(len(actions)):
		for i in range(size):
			for j in range(size):
				state0_ind = i*size + j
				for d in range(-1, 2):
					action = actions[(k + d)%4]
					state1_ind = (i + action[0])*size + j + action[1]
					if (k == 0 or k == 2) and d == 0 and (state1_ind >= (i+1)*5 or state1_ind < i*5) and state1_ind >= 0 and state1_ind < n_states: #test for left right
						transitions[k][state0_ind][state0_ind] += move_prob
					elif (k == 1 or k==3) and d != 0 and (state1_ind >= (i+1)*5 or state1_ind < i*5) and state1_ind >= 0 and state1_ind < n_states: #test up down
						transitions[k][state0_ind][state0_ind] += (1-move_prob)/2
					elif state1_ind >= 0 and state1_ind < n_states:		
						if d == 0:
							transitions[k][state0_ind][state1_ind] += move_prob
						else:
							transitions[k][state0_ind][state1_ind] += (1-move_prob)/2
					else:
						if d == 0:
							transitions[k][state0_ind][state0_ind] += move_prob
						else:
							transitions[k][state0_ind][state0_ind] += (1-move_prob)/2


	# for mat in transitions[0]:
	# 	print_as_grid(mat, 5, policy=False)
	# 	print()

	return transitions

def create_reward_matrix(grid):
	reward = np.zeros((len(grid)**2))
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == -1:
				reward[i*len(grid)+j] = -1
			elif grid[i][j] == 1:
				reward[i*len(grid)+j] = 1

	# print_as_grid(reward, 5, policy=False)

	return reward

def print_as_grid(my_vec, lake, dim, policy=True):
	if policy:
		my_vec = list(my_vec)
		for i in range(len(my_vec)):
			if my_vec[i] == 0:
				my_vec[i] = '<'
			if my_vec[i] == 1:
				my_vec[i] = '^'
			if my_vec[i] == 2:
				my_vec[i] = '>'
			if my_vec[i] == 3:
				my_vec[i] = 'v'
			if lake[int(i/5)][i%5] == -1:
				my_vec[i] = 'O'
			if lake[int(i/5)][i%5] == 1:
				my_vec[i] = 'X'

	for i in range(dim):
		ind0 = i*5
		ind1 = (i+1)*5
		print(my_vec[ind0:ind1])
	print()

def print_policy_vs_value(p_policy, v_policy):
	print_as_grid(p_policy)
	print()
	print_as_grid(v_policy)