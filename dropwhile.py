#!/usr/bin/env python3
# encoding: utf-8


def drop_while(p, xs):
	should_gather = False
	gathered = []
	for x in xs:
		if not p(x) or should_gather:
			should_gather = True
			gathered.append(x)
		"""if not p(x):
			should_gather = True
		if should_gather:
			gathered.append(x)"""
	return gathered
