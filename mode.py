#!/usr/bin/env python3

import sys

def input_num(prompt):
	return int(input(prompt))

counts = [0] * 10
print(
	'You will be asked to enter some integers between 1 and 10.',
	'When you are done, enter 0 to stop.')

while True:
	try:
		num = input_num('Enter an integer, or 0 to stop: ')
	except ValueError:
		print('Enter a valid integer.')
		continue

	if num == 0:
		break

	if num not in range(1, 11):
		print('Enter an integer in range.')
		continue

	counts[num-1] += 1

mode = max(range(len(counts)), key=lambda num: counts[num]) + 1

max_count = 0
mode = 0
for num, count in enumerate(counts, 1):
	if count > max_count:
		max_count = count
		mode = num

if mode == 0:
	print('No numbers entered.')
	sys.exit(1)

print('This number occurred the most:', mode)
