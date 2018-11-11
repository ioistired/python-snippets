#!/usr/bin/env python3
# encoding: utf-8

class Foo:
	def __init__(self):
		return 1


def main():
	x = Foo()
	print(type(x))


if __name__ == '__main__':
	main()
