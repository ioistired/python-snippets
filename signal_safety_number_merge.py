#!/usr/bin/env python3

import itertools
import functools

def chunk(n, seq):
	"""split seq into n equal-ish sized parts. The result, when flattened, shall be equal to seq."""
	chunk_len = len(seq) // n + 1
	for chunk_start in range(0, len(seq), chunk_len):
		yield seq[chunk_start : chunk_start + chunk_len]

halve = functools.partial(chunk, 2)

def merge_safety_numbers(a, b):
	"""Given your safety numbers with two people, return the safety numbers between those two people."""
	a_fingerprints = set(map(str.strip, halve(a)))
	b_fingerprints = set(map(str.strip, halve(b)))

	# a_fingerprints | b_fingerprints = all three parties' fingerprint (mine, alice's, and bob's)
	# a_fingerprints & b_fingerprints = {my fingerprint}
	a_b_fingerprints = a_fingerprints.symmetric_difference(b_fingerprints)
	assert len(a_b_fingerprints) == 2
	return ' '.join(sorted(a_b_fingerprints))

def test_merge_safety_numbers():
	assert merge_safety_numbers('823 456 987 654', '767 530 823 456') == '767 530 987 654'

def main():
	import sys
	args = sys.argv[1:]
	print(merge_safety_numbers(*args))

if __name__ == '__main__':
	main()
