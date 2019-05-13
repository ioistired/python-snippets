#!/usr/bin/env python3
# encoding: utf-8

from typing import Iterable

from functional_dependency import FunctionalDependency

def closure(attrs: frozenset, fds: Iterable[FunctionalDependency]):
	"""find the closure of a set of attributes under a given set of functional dependencies"""
	closure = attrs
	while True:
		original_size = len(closure)

		for dep in fds:
			if dep.lhs.issubset(closure):
				closure |= dep.rhs

		if len(closure) == original_size:
			break

	return closure

if __name__ == '__main__':
	FD = FunctionalDependency
	fds = [FD('A','B'), FD('A','C'), FD('CG', 'H'), FD('CG', 'I'), FD('B', 'H')]
	print(closure(frozenset('AG'), fds))
	assert closure(frozenset('AG'), fds) == frozenset('ABCGHI')
