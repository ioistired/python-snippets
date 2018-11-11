#!/usr/bin/env python3
# encoding: utf-8

import os
import timeit

nbytes = 5
secret = bytearray(os.urandom(nbytes))

# intentionally insecure
def validate(a, b):
	if len(a) != len(b):
		return False
	for x, y in zip(a, b):
		if x != y:
			return False
	return True

def check(a, b):
	return timeit.timeit(lambda: validate(a, b), number=10000)

def brute_force():
	current_secret = bytearray(nbytes)
	# time taken to validate a correct secret
	correct_time = check(current_secret, current_secret)

	i = 0

	while True:
		correct = validate(current_secret, secret)
		if correct:
			return bytes(current_secret)

		current_time = check(current_secret, secret)
		if current_time >= correct_time:
			return bytes(current_secret)

		if i >= nbytes:
			print(current_secret)
			print(secret)
			return None  # correct secret not found

		times = {}
		for byte in range(256):
			current_secret[i] = byte
			times[byte] = check(current_secret, secret)

		correct_byte, current_time = max(times.items(), key=lambda pair: pair[1])
		current_secret[i] = correct_byte
		i += 1

if __name__ == '__main__':
	print(brute_force())
