#!/usr/bin/env python3
# encoding: utf-8

def parse_bin(n: bytes) -> int:
	"""convert a C string representing binary to an unsigned integer"""

	# this is written in a highly imperative style
	# to make it easy to translate to MIPS
	p = 0
	i = 0
	while True:
		c = n[i]

		if c == ord('1'):
			p |= 1
		elif c == ord('0'):
			pass  # |= 0
		elif c == 0:  # null byte
			p >>= 1
			break
		else:
			raise ValueError('invalid string representing binary')

		p <<= 1
		i += 1

	return p

if __name__ == '__main__':
	import sys
	n = sys.argv[1].encode('ascii') + b'\0'
	print(parse_bin(n))
