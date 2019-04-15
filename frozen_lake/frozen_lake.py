import turtle
import time
import numpy as np

class Agent():
	def __init__(self, p_move):
		self.coords = (0, 0)
		self.actions = [(0, -1), (1, 0), (0, 1), (1, 0)] #L, U, R, D

	def move(self, direction, lake_size):
		val = np.random.rand()
		if val < p_move - 1 and val >= (p_move - 1)/2:
			direction = (direction + 1) % 4
		elif val < (p_move - 1)/2:
			direction = (direction - 1) % 4
		new_coords = [self.coords[i] + self.actions[direction][i] for i in range(2)]
		if self.is_valid_move(new_coords, lake_size):
			self.coords = new_coords

	def is_valid_move(self, coords, lake_size):
		for i in range(len(coords)):
			if coords[i] < 0 or coords[i] >= lake_size:
				return False
		return True


class FrozenLake:
	def __init__(self, size, p_hole, random_state):
		self.random_state = random_state
		self.size = size
		self.p_hole = p_hole
		self.lake_init(random_state)
		self.visualize_lake()
		self.agent = Agent(1)

	def lake_init(self, random_state=None):
		self.lake = [[0 for i in range(self.size)] for j in range(self.size)]
		if random_state:
			np.random.seed(random_state)
		for i in range(self.size):
			for j in range(self.size):
				if np.random.rand() <= self.p_hole:
					self.lake[i][j] = -1
				else:
					self.lake[i][j] = -0.04
		self.lake[self.size-1][self.size-1] = 1

	def step(self, action=None):
		self.agent_turtle.undo()
		if not action:
			action = np.random.randint(0, 4)
		self.agent.move(action, self.size)
		state = self.agent.coords
		reward = self.lake[state[0]][state[1]]
		print(reward)
		self.agent_turtle.goto(state)
		self.agent_turtle.stamp()
		if reward == 1 or reward == -1:
			self.reset()
		return (state, reward)

	def reset(self):
		self.agent_turtle.undo()
		self.agent_turtle.goto((0,0))
		self.agent_turtle.stamp()
		self.agent = Agent(1)

	def visualize_lake(self):
		window = turtle.Screen()
		window.bgcolor('white')
		turtle.setworldcoordinates(-1, -5, 5, 1)
		turtle.clearscreen()

		turtle.tracer(0, 0)
		lake_turtle = turtle.Turtle()
		lake_turtle.shape('square')
		lake_turtle.color('#add8e6')
		lake_turtle.penup()
		lake_turtle.resizemode('user')
		lake_turtle.shapesize(11)
		hole_turtle = turtle.Turtle()
		hole_turtle.shape('circle')
		hole_turtle.color('#0077be')
		hole_turtle.penup()
		hole_turtle.resizemode('user')
		hole_turtle.shapesize(7)
		goal_turtle = turtle.Turtle()
		goal_turtle.shape('square')
		goal_turtle.color('red')
		goal_turtle.fillcolor('#add8e6')
		goal_turtle.penup()
		goal_turtle.resizemode('user')
		goal_turtle.shapesize(9)
		star_turtle = turtle.Turtle()
		star_turtle.shape('square')
		star_turtle.color('green')
		star_turtle.fillcolor('#add8e6')
		star_turtle.penup()
		star_turtle.resizemode('user')
		star_turtle.shapesize(9)

		for i in range(self.size):
			for j in range(self.size):
				lake_turtle.goto((j, -i))
				lake_turtle.stamp()
				if self.lake[i][j] == -1:
					hole_turtle.goto((j, -i))
					hole_turtle.stamp()
		goal_turtle.goto((self.size-1, -self.size+1))
		goal_turtle.stamp()
		star_turtle.goto((0, 0))
		star_turtle.stamp()

		turtle.tracer(1, 1)
		agent_turtle = turtle.Turtle()
		agent_turtle.shape('circle')
		agent_turtle.color('#EED893')
		agent_turtle.penup()
		agent_turtle.resizemode('user')
		agent_turtle.shapesize(3)
		agent_turtle.goto((0, 0))
		agent_turtle.stamp()
		self.agent_turtle = agent_turtle


# lake = FrozenLake(5, .2, random_state=10)
# for i in range(100):
# 	lake.step()

# programpause = input("press enter to continue")











