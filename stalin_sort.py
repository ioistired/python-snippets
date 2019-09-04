def stalin_sort(list):
	to_delete = []
	for i in range(len(list) - 1):
		if list[i] >= list[i + 1]:
			to_delete.append(i)
	for i in reversed(to_delete):
		del list[i]
