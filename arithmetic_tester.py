#!/usr/bin/env python3
# encoding: utf-8

# public domain

import random

"""
spec:
[11:37 PM] nick: can you write a python function that
just generates a really long string containing all numbers and +-*/?

int type: signed 64 bit
"""

def arithmetic_gen(operand_count):
	operands = []
	rand_num = lambda: str(random.randrange(-2**64, 2**63))
	for _ in range(operand_count):
		operands.append(rand_num())
		operands.append(random.choice('+-*/'))
	operands.append(rand_num())
	return ''.join(operands)

def test_case_gen(operand_count=10_000):
	expr = arithmetic_gen(operand_count)
	try:
		# don't deal with floats
		result = eval(expr.replace('/', '//'))
	except ArithmeticError as e:
		result = type(e)
	return result, expr

if __name__ == '__main__':
	import sys
	op_count = int(sys.argv[2])
	print('expected result\texpr')
	for _ in range(int(sys.argv[1])):
		result, expr = test_case_gen(op_count)
		print(result, expr, sep='\t')
