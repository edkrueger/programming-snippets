"""Currying"""

import time

def add(x, y):
	return x + y

def curried_add(x):
	def add_y_to_x(y):
		return x + y
	return add_y_to_x

def slow_computation(x):
	time.sleep(1)
	return x

def slow_add(x, y):
	return slow_computation(x) + y

def slow_add_curried(x):
	x = slow_computation(x)
	def add_y_to_x(y):
		return x + y
	return add_y_to_x

if __name__ == "__main__":
	assert add(1, 2) == 3
	assert curried_add(1)(2) == 3

	# # takes about 3s
	assert slow_add(1, 2) == 3 # take about 1s
	assert slow_add(1, 3) == 4 # take about 1s
	assert slow_add(1, 5) == 6 # take about 1s

	# # takes about 1s
	slow_add_y_to_x = slow_add_curried(1) # take about 1s
	assert slow_add_y_to_x(2) == 3 
	assert slow_add_y_to_x(3) == 4
	assert slow_add_y_to_x(5) == 6
