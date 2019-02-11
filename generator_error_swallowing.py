#!/usr/bin/env python3
# encoding: utf-8

def error():
	yield 1
	raise Exception

def thing():
	return error()

def main():
	for x in thing():  # thing won't be in the traceback
		pass

if __name__ == '__main__':
	main()
