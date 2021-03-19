count = 0

def increment_counter():
	"""Should skip 13."""

	global count

	if count != 12:
		count += 1
	else:
		count += 2

	return count

class Counter():
	"""A counter"""
	def __init__(self):
		self.count = 0

	def increment_counter(self):

		if self.count == 12:
			self.count += 2
		else:
			self.count +=1

	def get_count(self):
		return self.count		

def increment_counter_pure(count):
	"""Should Skip 13."""

	return count + 1 if count != 12 else count + 2

if __name__ == "__main__":

	# An Object
	# have to get it into a state before testing the key behavior
	counter = Counter()

	# increment 13 times
	for _ in range(13):
		counter.increment_counter()

	assert counter.get_count() == 14

	# Not a pure function
	# could have written this as a loop
	# but still have to get it into a state before testing the key behavior
	assert increment_counter() == 1
	assert increment_counter() == 2
	assert increment_counter() == 3
	assert increment_counter() == 4
	assert increment_counter() == 5
	assert increment_counter() == 6
	assert increment_counter() == 7
	assert increment_counter() == 8
	assert increment_counter() == 9
	assert increment_counter() == 10
	assert increment_counter() == 11
	assert increment_counter() == 12
	assert increment_counter() == 14

	assert increment_counter_pure(12) == 14
