import numpy as py
from scipy.special import comb
import math

class Bernoulli:
	def __init__(self, p):
		self.p = p

	#value: {0, 1}
	def P(self, value):
		if value != 1 and value != 0:
			return None
		else:
			return self.p**value * (1 - self.p)**(1 - value)

class Binomial:
	def __init__(self, n, p):
		self.n = n
		self.p = p

	def P(self, k):
		if self.n < k:
			return None
		else:
			return comb(self.n, k)*(self.p)**k * (1 - self.p)**(self.n - k)

class Poisson:
	def __init__(self, lamb):
		self.lamb = lamb

	def P(self, k):
		if k < 0:
			return None
		else:
			return (math.exp(-self.lamb)*(self.lamb**k))/(math.factorial(k))


