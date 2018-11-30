#!/usr/bin/env python3
# encoding: utf-8

# Public Domain, search for cc-0 online for full terms

import functools
import string
import sys

# allows "0x3D" or "0b100" as input
parse_int = functools.partial(int, base=0)

def err(*args, **kwargs):
	print(*args, **kwargs, file=sys.stderr)

# skip ABCDEF and turn the "abcdef" uppercase
CHARSET = string.hexdigits.upper()[:-6]













def int_to_hex(x: int, bitsize=16):
	bitsize -= 4  # diagram needed to explain this const, xd
	shamt = bitsize

	while shamt >= 0:
		t0 = x  # preserve x since we modify a copy of it in place each loop
		t0 >>= shamt  # get the hexit we want on the "right" (LSB position)
		t0 &= 0xF  # ignore all other bits to the "left" ("more significant bit" positions)

		yield CHARSET[t0]

		shamt -= 4  # let's work on the next hexit in the next loop

















def main(x: str, bitsize: str = None) -> int:
	x = parse_int(x)

	extra_args = []
	if bitsize is not None:
		bitsize = parse_int(bitsize)
		extra_args.append(bitsize)

	hex = int_to_hex(x, *extra_args)
	print(''.join(hex))

	return 0

if __name__ == '__main__':
	argv_without_filename = sys.argv[1:]
	sys.exit(main(*argv_without_filename))
