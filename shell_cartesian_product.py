#!/usr/bin/env python3
# encoding: utf-8

import re as _re

def expand(str) -> (str, str):
	"""expand a string containing one non-nested cartesian product strings into two strings

	>>> expand('foo{bar,baz}')
	('foobar', 'foobaz')
	>>> expand('{old,new}')
	('old', 'new')
	>>> expand('uninteresting')
	'uninteresting'
	"""

	match = _re.search(r'{([^{}]*),([^{}]*)}', str)
	if match is None:
		return str

	return (
		str[:match.start()] + match.group(1) + str[match.end():],
		str[:match.start()] + match.group(2) + str[match.end():]
	)

def _test():
	import doctest
	doctest.testmod()

if __name__ == '__main__':
	_test()
