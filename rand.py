import numpy as np
import random

def rand (n):
	return random.randint(0, n-1)

def rand_k (k, n):
	l = list(range(0, n))
	selection = []
	for i in range(k):
		index = random.randint(0, len(l) - i -1 )
		selection.append(l[index])
		del l[index]
	return selection

def bivariate_random_generator (dist):
	x_axis = []
	y_axis = []
	for row in dist:
		y_axis.append(sum(row))
	for i in range(len(dist[0])):
		x_axis.append(sum(row[i] for row in dist))
	print(sum(x_axis))
	x = np.random.choice(np.arange(1, 6), p=x_axis)
	y = np.random.choice(np.arange(1, 6), p=y_axis)
	return [x, y]

dist = [[0.0266, 0.0697, 0.0775, 0.0313, 0.0101],
		[0.0283, 0.0761, 0.0739, 0.0566, 0.0362],
		[0.0109, 0.0337, 0.0552, 0.0780, 0.0740],
		[0.0014, 0.0093, 0.0309, 0.0750, 0.0698],
		[0.0001, 0.0028, 0.0124, 0.0318, 0.0284]]
print(bivariate_random_generator(dist))