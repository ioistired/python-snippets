#!/usr/bin/env python3
# encoding: utf-8

# based on someone elses soln

class Goal(int):
	def __call__(self, x=None):
		if x is None:
			return type(self)(self+1)
		return f'g{"o"*self}{x}'

g = Goal()


def main():
	"""self-test"""
	if not __debug__:
		raise AssertionError('debug mode is off, so no tests will be run')

	assert g()()()('al') == 'goooal'
	assert g()()('al') == 'gooal'
	assert g()('al') == 'goal'
	assert g('al') == 'gal'
	assert g('houl') == 'ghoul'


if __name__ == '__main__':
	main()
