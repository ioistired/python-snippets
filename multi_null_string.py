#!/usr/bin/env python3
# encoding: utf-8

import os
import sys

STDOUT = sys.stdout.fileno()

def main(text: bytes):
i = 0
while True:
	while text[i] != 0:
		# indexing a bytearray yields ints not bytes
		os.write(STDOUT, bytes(text[i]))
		sys.stdout.flush()
		i += 1
	os.write(STDOUT, b'\n')

	i += 1
	if not text[i]:
		break

if __name__ == '__main__':
	main(sys.argv[1].encode('utf-8'))
