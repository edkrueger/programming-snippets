def my_sum(*args):

	total = 0

	for e in args:
		total + e

	return total

def my_sum(*args):
	return sum(args)

if __name__ == "__main__":
	my_sum(1, 2, 3) == sum([1, 2, 3])
	my_sum(1, 2, 3, 4) == sum([1, 2, 3, 4])
