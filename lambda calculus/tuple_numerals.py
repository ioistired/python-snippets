#!/usr/bin/env python3
# encoding: utf-8

from functools import lru_cache
import operator

memoize = lru_cache(maxsize=None)

ZERO = ()

def succ(n: tuple):
	return (n,)

ONE = succ(ZERO)

def pred(n: tuple):
	if not n:
		return ZERO  # sorry, no negative numbers yet
	return n[0]
	# equivalently: n and n[0]

def encode(n: int):
	if n <= 0:
		return ZERO
	return succ(encode(n-1))

# while more elegant, the above is inefficient in python

def encode(n: int):
	out = ZERO
	for _ in range(n):
		out = succ(out)
	return out

def decode(n) -> int:
	if n == ZERO:
		return 0
	return 1 + decode(pred(n))

def decode(n) -> int:
	out = 0
	while n != ZERO:
		n = pred(n)
		out += 1
	return out

def add(x, y):
	# additive identity
	if x == ZERO:
		return y
	elif y == ZERO:
		return x

	return add(pred(x), succ(y))

def add(x, y):
	if y == ZERO:
		return x

	while x != ZERO:
		x = pred(x)
		y = succ(y)

	return y

def sub(x, y):
	if y == ZERO:
		return x
	return sub(pred(x), pred(y))

# less elegant, more efficient
def sub(x, y):
	while y != ZERO:
		x = pred(x)
		y = pred(y)
	return x

def eq(x, y):
	return le(x,y) and le(y,x)

def le(x, y):
	return sub(x, y) == ZERO

def ge(x, y):
	return gt(x, y) or eq(x, y)

def lt(x, y):
	return le(x, y) and gt(y, x)

def gt(x, y):
	return sub(x, y) != ZERO


# FIXME 7*3 != 1.5 * 2**7
def mul(x, y):
	if x == ZERO or y == ZERO:
		return ZERO
	if x == ONE:
		return y
	elif y == ONE:
		return x

	return mul(add(x, x), pred(y))

def div(x, y):
	if y == ZERO:
		raise ZeroDivisionError
	if y == ONE:
		return x

	def aux(x,y,i):
		if x == ZERO:
			return i
		return aux(sub(x,y),y,succ(i))

	return aux(x,y,ZERO)

def div(x,y):
	if y == ZERO:
		raise ZeroDivisionError
	if y == ONE:
		return x  # optimization

	i = ZERO
	while True:
		x = sub(x,y)
		if x == ZERO:
			break  # avoid e.g. 0/1 = 1
		i = succ(i)
	return i

def mul(x, y):
	if x == ZERO or y == ZERO:
		return ZERO

	acc = x
	i = pred(y)
	while i != ZERO:
		acc = add(acc, x)
		i = pred(i)
	return acc

def pow(x, y):
	if x == ZERO and y == ZERO:
		raise ArithmeticError('cannot compute ZERO^ZERO')

	acc = x
	i = y
	while i != ZERO:
		acc = mul(acc,x)
		i = pred(i)
	return acc

def many_pairs(n):
	for x in range(n):
		for y in reversed(range(n)):
			yield x, y

def test_cmp():
	for x, y in many_pairs(100):
		tx, ty = encode(x), encode(y)
		assert (x == y) == eq(tx, ty)
		assert (x < y) == lt(tx, ty)
		assert (x <= y) == le(tx, ty)
		assert (x > y) == gt(tx, ty)
		assert (x >= y) == ge(tx, ty)

def test_op(int_op, tuple_op):
	for x, y in many_pairs(100):
		assert (
			max(int_op(x, y), 0)
			== decode(tuple_op(encode(x), encode(y)))
		), (x, y)

def test_ops():
	ops = (
		(operator.add, add),
		(operator.sub, sub),
		(operator.mul, mul),
		(operator.floordiv, div),
		(operator.pow, pow),
	)
	for int_op, tuple_op in ops:
		test_op(int_op, tuple_op)
