def bad_append_squares(in_list, out_list=[]):
	"""This is not."""

	for e in in_list:
		out_list.append(e**2)
	return out_list

def good_append_squares(in_list, out_list=None):
	"""This is pure function."""

	out_list_ = out_list if out_list else []

	for e in in_list:
		out_list_.append(e**2)

	return out_list_


if __name__ == "__main__":

	# in bad_append_squares the [] emulates a static varialbe
	# we can argue if its actually a non-local of a static local,
	# but that is pedantic

	# The function's arguemnts are not in its scope,
	# [] is being made outside of the functions scope

	# non-goofy use of this function
	assert bad_append_squares([1,2,3], [1, 2, 3]) == [1, 2, 3, 1, 4, 9]

	# no problem
	# we are passing a different empty list every time we call the function
	assert bad_append_squares([1,2,3], []) == [1, 4, 9]
	assert bad_append_squares([1,2,3], []) == [1, 4, 9]


	# we have a problem
	# the reason why is that when the function is declared it point to a single []

	# not being a pure function,
	# we have the same function call resulting in two differnt outputs
	# in order to test both behaviors we have to rely on context,
	# in other words if I ran these lines in a different order,
	# then, I'd get a different result

	# tlrd: if I switch the order of the assetions,
	# the test no longer works as intended

	# tldr2: with pure functions, you don't have to setup or mock-up a state

	assert bad_append_squares([1,2,3]) == [1, 4, 9]
	# here we are testing for known bad behavior
	assert bad_append_squares([1,2,3]) == [1 , 4, 9, 1, 4, 9]

	# no problem
	good_append_squares([1,2,3], [])
	good_append_squares([1,2,3], [])

	# no problem
	# automatically creates new []
	good_append_squares([1,2,3])
	good_append_squares([1,2,3])