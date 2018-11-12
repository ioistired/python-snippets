#!/usr/bin/env python3
# encoding: utf-8

from functools import partial

def _generate_emoji_ranges(lines):
	for line in lines:
		if not line or line == '\n' or line.startswith('#'):
			continue

		yield _inclusive_range(*_parse_line(line))

def _parse_line(line):
	"""parse two nums from a line of EmojiData.txt

	input format: hex number".."hex number "#" comment
	or:           hex number "#" comment
	output: iterable of one or two ints
	"""
	nums = line.split()[0].split('..')
	return map(_hex_to_int, nums)

_hex_to_int = partial(int, base=16)

def _inclusive_range(start, stop=None, step=1):
	"""return a range i <= j <= k
	if k is not provided, return a range containing only i.
	step is also supported and defaults to 1
	"""
	if stop is None:
		stop = start
	stop += 1

	return range(start, stop, step)

with open('data/emoji-data.txt') as f:
	EMOJI_RANGES = tuple(_generate_emoji_ranges(f))
del f

def is_emoji(s: str):
	"""return whether a *single code point* is an emoji.
	detecting multi-code point emojis is non-trivial"""

	ord_s = ord(s)  # optimization
	return any(ord_s in range for range in EMOJI_RANGES)

def _bool_status(x: bool) -> int:
	# in shell scripting, 0 is true
	# in py its the opposite
	return int(not x)

if __name__ == '__main__':
	import sys

	sys.exit(_bool_status(is_emoji(sys.argv[1])))
