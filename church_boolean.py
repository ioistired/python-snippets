#!/usr/bin/env python3
# encoding: utf-8

import functools as _functools
_memoize = _functools.lru_cache(maxsize=None)


def true(a, b):
	return a

def false(a, b):
	return b


def not_(a):
	return a(false, true)


def and_(a, b):
	return a(b, false)


def or_(a, b):
	return a(true, b)


def xor(a, b):
	return a(not_(b), b)


def if_(predicate, then, else_):
	return predicate(then, else_)


@_memoize
def fib(n):
	if_(lambda: 0<=n<2,
	lambda: 1,
	lambda: fib(n-1) + fib(n-2))()


def test_not():
	assert not_(true) == false
	assert not_(false) == true


def test_and():
	assert and_(false, false) == false
	assert and_(false, true) == false
	assert and_(true, false) == false
	assert and_(true, true) == true


def test_or():
	assert or_(false, false) == false
	assert or_(false, true) == true
	assert or_(true, false) == true
	assert or_(true, true) == true


def test_xor():
	assert xor(false, false) == false
	assert xor(false, true) == true
	assert xor(true, false) == true
	assert xor(false, false) == false