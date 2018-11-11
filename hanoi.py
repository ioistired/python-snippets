#!/usr/bin/env python3
# encoding: utf-8

def pr(n):
	if n > 0:
		pr(n - 1)
		print(n)
		pr(n - 1)
	else:
		pass

def hanoi(n):
	if n == 1:
		return [1]
	else:
		return hanoi(n - 1) + [n] + hanoi(n - 1)

def hanoi(n):
	def aux(n, acc):
		if n == 1:
			return acc
		else:
			return aux(n - 1, acc + [n] + acc)
	return aux(n, [1])


def format_hanoi(seq):
	formatted = ''
	for i, n in enumerate(seq):
		which_way = "left" if i % 2 else "right"
		formatted += "Move disk {} to the {}.\n".format(n, which_way)
	return formatted


if __name__ == "__main__":
	import sys
	print(hanoi(int(input("n? "))), end='')
