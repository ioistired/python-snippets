#!/usr/bin/env python3
# encoding: utf-8

import functools
import typing

def make_node(data, next=None):
	if next is None:
		return (data,)
	return (data,next)

nums = make_node(0, make_node(1, make_node(2)))

def linkedlist(data: typing.Sequence):
	if not data:
		return ()
	if len(data) == 1:
		return make_node(data[0])
	return make_node(data[0], linkedlist(data[1:]))

def linkedlist(data: Iterable):
	if not data:
		return ()
	data = iter(data)
	return make_node(next(data), data)

linkedlist = lambda data: reduce(make_node, data, ())
