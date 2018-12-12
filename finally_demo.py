#!/usr/bin/env python3
# encoding: utf-8

def main():
	try:
	     raise ValueError
	except:
	     print('hi')
	     0 / 0
	finally:
	     return 1

if __name__ == '__main__':
	print(main())
