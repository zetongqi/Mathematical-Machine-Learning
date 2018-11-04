import numpy as np
import math
import sys

d = int(sys.argv[1])
l = int(sys.argv[2])
n = int(sys.argv[3])
if l > d:
	print("error: l must be smaller than d")

cnt = 0
for i in range(n):
	x = np.random.uniform(0, d/2, 1)
	theta = np.random.uniform(0, math.pi/2, 1)
	if x < (l/2)*math.sin(theta):
		cnt += 1
pi_est = (2*l)/(d*(cnt/n))
print(pi_est)