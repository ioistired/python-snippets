#!/usr/bin/env python3

def reverse_range(r):
	return range(r.start + (len(r) - 1) * r.step, r.start - r.step, -r.step)

def test():
	for r in (
		range(12),
		range(5, 13, 3),
		range(13, 5, -3),
	):
		assert reverse_range(reverse_range(r)) == r
		assert list(reversed(r)) == list(reverse_range(r))

if __name__ == '__main__':
	test()
