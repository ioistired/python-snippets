#!/usr/bin/env python3
# encoding: utf-8


def encode(n):
	i = 0
	acc = {}
	while i < n:
		acc[()] = acc.copy()
		i += 1
	return acc

def encode(n: int):
	def aux(i, acc={}):
		if i < n:
			return aux(i+1, succ(acc))
		else:
			return acc
	return aux(0)


def decode(n: dict) -> int:
	i = 0
	while () in n:
		n = pred(n)
		i += 1
	return i

def decode(n: dict) -> int:
	def aux(i, n):
		if () not in n:
			return i
		else:
			return aux(i+1, pred(n))
	return aux(0, n)

def decode(n: dict):
	if not n:
		return 0
	return 1 + decode(pred(n))

def pred(n: dict) -> dict:
	if not n:
		# no negative numbers yet
		return n
	return n[()]

def succ(n: dict) -> dict:
	# copy prevents self referential dicts
	return {(): n.copy()}

def add(x: dict, y: dict) -> dict:
	# dumb way
	return encode(decode(x)+decode(y))

# XXX still mutates x > 0
def add(x: dict, y: dict) -> dict:
	"""add two dict numerals and return a new dict numeral

	>>> x = {(): {(): {}}}
	>>> y = {(): {}}
	>>> add(x, y)
	{(): {(): {(): {}}}}
	"""

	# handle the additive identity
	if not x:
		return y
	elif not y:
		return x

	# do not mutate args
	x = x.copy()
	# keep a pointer around so we can traverse without fear
	# of losing x
	orig_x = x

	while () in x:
		x = pred(x)

	# hook y up to the end of x
	x[()] = pred(y).copy()
	return orig_x


# def add(x: dict, y: dict) -> dict:
# 	...
