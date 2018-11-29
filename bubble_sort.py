#!/usr/bin/env python3

import random

def bubble_sort(list):
	for i in range(len(list) - 1):
		for j in range(i+1, len(list)):
			if list[i] > list[j]:
				swap(list, i, j)

def swap(list, i, j):
	list[i], list[j] = list[j], list[i]

random_list = lambda: [random.randrange(100) for _ in range(10)]

list = random_list()
sorted_list = sorted(list)
bubble_sort(list)

print('bubble sorted:'.ljust(20), list)
print('tim sorted:'.ljust(20), sorted_list)
print('equal?:'.ljust(20), list == sorted_list)

for _ in range(1000):
	list = random_list()
	bubble_sort(list)
	assert sorted(list) == list
