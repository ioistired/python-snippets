#!/usr/bin/env python3

class UniqueIdDict(dict):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.counter = 0

	def __missing__(self, key):
		self[key] = ret = self.counter
		self.counter += 1
		return ret

def test():
	d = UniqueIdDict()
	a_val = d['a']
	assert d['a'] == a_val
	b_val = d['b']
	assert b_val == d['b']
	assert a_val != b_val

if __name__ == '__main__':
	test()
