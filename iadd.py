#!/usr/bin/env python3
# encoding: utf-8

class NoisyList(list):
	def __setitem__(self, i, x):
		print(f'self[{i}] = {x}')
		super().__setitem__(i, x)

	def __iadd__(self, other):
		print(f'self += {other}')
		super().__iadd__(other)
		# note: no return self!

def main():
	nums = NoisyList([NoisyList([0]), NoisyList([2,3])])
	nums[0] += [1]
	assert nums[0] is None  # dumb af behavior

if __name__ == '__main__':
	main()
