#!/usr/bin/env python3
# encoding: utf-8

def grade(score):
	letter = 'FFFFFFDCBA'[int(score*10)]
	pm = '----- ++++'[int(score*100)%10]
	return letter+pm


if __name__ == '__main__':
	import sys

	print(grade(float(sys.argv[1])))
