# no mutation queue
queue = [1, 2, 3, 4, 5, 6]

while queue:
	e, *queue = queue
	print(e)

# mutation
queue = [1, 2, 3, 4, 5, 6]

while queue:
	e = queue.pop(0)
	print(e)
