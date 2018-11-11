#!/usr/bin/env python3
# encoding: utf-8

import fileinput


def fix_sums():
	"""fixes a checksums file in this format:
	\d4e9b804eb556f8140b17921 *C:\\TV\\My Show.mkv
	\885083f72a4211a6f95eb380 *C:\\Movies\\My Adventure.mkv

	and replaces it with something more sensible:
	d4e9b804eb556f8140b17921 My Show.mkv
	885083f72a4211a6f95eb380 My Adventure.mkv
	"""

	# input() gets filenames from sys.argv[1:] by default
	with fileinput.input(inplace=True) as f:
		for line in f:
			line = line.split('*')
			sum = line[0][1:] # remove leading \
			filename = line[1].split(r'\\')[-1] # last component after last \\
			print(sum + filename, end='') # filename already has a newline


def main():
	import sys

	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<filename[s]>', file=sys.stderr)
		sys.exit(1)

	fix_sums()


if __name__ == '__main__':
	main()
