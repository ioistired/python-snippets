#!/usr/bin/env python3
# encoding: utf-8

import typing

def rstrip_in_place(xs: typing.List[typing.T], predicate: typing.Callable[[typing.T], bool]) -> None:
	"""remove elements from the right of xs until predicate no longer holds"""
	while xs and predicate(xs[-1]):
		xs.pop()

def rstrip(xs: typing.List[typing.T], predicate: typing.Callable[[typing.T], bool]) -> typing.List[typing.T]:
	copied = xs.copy()
	rstrip_in_place(copied, predicate)
	return copied

def test():
	assert rstrip([5, 4, 3, 0, False], lambda x: not x) == [5, 4, 3]
	assert rstrip([5, 4, 3], lambda x: not x) == [5, 4, 3]
	assert rstrip(list('foo bar  \n'), str.isspace) == list('foo bar')
	assert rstrip(list('foo bar'), str.isspace) == list('foo bar')
	assert rstrip(list(''), str.isspace) == list('')

if __name__ == '__main__':
	test()
