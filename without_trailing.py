#!/usr/bin/env python3

import sys

import more_itertools

def without_trailing(it, *, trailing, _exhausted=object()):
	"""yield all elements of it, except for the last one, if the last one == trailing."""
	it = more_itertools.peekable(it)
	for x in it:
		if it.peek(_exhausted) is _exhausted and x == trailing:
			return
		yield x

def main():
	num_lines = more_itertools.ilen(without_trailing(sys.stdin, trailing='\n'))
	print(f'Without a trailing newline, there were {num_lines} lines in my input.')

if __name__ == '__main__':
	main()
