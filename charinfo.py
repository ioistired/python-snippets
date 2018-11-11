#!/usr/bin/env python3.6
# encoding: utf-8
# Copyright 2015 Rapptz
# MIT Licensed
# Original source: https://github.com/Rapptz/RoboDanny/blob/c8fef9f07145cef6c05416dc2421bbe1d05e3d33/cogs/meta.py#L57-72

import unicodedata


def charinfo(characters):
	"""Shows you information about a number of characters."""

	def info(c):
		# get hexadecimal form
		digit = f'{ord(c):x}'
		name = unicodedata.name(c, 'Name not found.')
		return f'\\U{digit:>08}: {name} - {c} \N{EM DASH} <http://www.fileformat.info/info/unicode/char/{digit}>'

	return '\n'.join(map(info, characters))


def main():
	import sys
	if len(sys.argv) > 1:
		print(charinfo(' '.join(sys.argv[1:])))
	else:
		print(charinfo(sys.stdin.read()))


if __name__ == '__main__':
	main()
