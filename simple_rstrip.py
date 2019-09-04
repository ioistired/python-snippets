#!/usr/bin/env python3
# encoding: utf-8

import typing

def rstrip_in_place(predicate: typing.Callable[[typing.T], bool], xs: typing.List[typing.T]) -> None:
	"""remove elements from the right of xs until predicate no longer holds"""
	while xs and predicate(xs[-1]):
		xs.pop()

def rstrip(predicate: typing.Callable[[typing.T], bool], xs: typing.Iterable[typing.T]) -> typing.List[typing.T]:
	copied = list(xs)
	rstrip_in_place(predicate, copied)
	return copied

def test():
	assert rstrip([5, 4, 3, 0, False], lambda x: not x) == [5, 4, 3]
	assert rstrip([5, 4, 3], lambda x: not x) == [5, 4, 3]
	assert rstrip(list('foo bar  \n'), str.isspace) == list('foo bar')

if __name__ == '__main__':
	test()
