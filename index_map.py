#!/usr/bin/env python3
# encoding: utf-8

import typing

# inspired by `for i, d[i] in enumerate(xs): pass`
def index_map(xs: typing.List[typing.T]) -> typing.Dict[typing.T, int]:
	d = {}
	for x, d[x] in map(reversed, enumerate(xs)):
		pass
	return d

def main():
	import string
	import sys

	if len(sys.argv) < 2:
		print('usage:', sys.argv[0], '<lowercase letter of the English alphabet>')
		sys.exit(1)

	letters_to_positions = index_map(string.ascii_lowercase)
	# "alphabet[12] == 'm'"
	print(f'alphabet[{letters_to_positions[sys.argv[1]]}] == {sys.argv[1]!r}')
	sys.exit(0)

if __name__ == '__main__':
	main()
