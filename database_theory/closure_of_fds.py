#!/usr/bin/env python3
# encoding: utf-8

import itertools

from functional_dependency import FunctionalDependency

def augment(fd, attr):
	if isinstance(attr, (set, frozenset)):
		return FunctionalDependency(fd.lhs | attr, fd.rhs | attr)
	return FunctionalDependency(fd.lhs | {attr}, fd.rhs | {attr})

def reflexive(attrs, permutations=None):
	permutations = permutations or itertools.permutations(attrs)

	for attr_set in itertools.permutations(attrs):
		yield FunctionalDependency(attrs, attr_set)

def transitive(fd1, fd2):
	if fd1.rhs == fd2.lhs:
		return FunctionalDependency(fd1.lhs, fd2.rhs)

	if fd2.rhs == fd1.lhs:
		return FunctionalDependency(fd2.lhs, fd1.rhs)

	raise ValueError('fd1 and fd2 are not transitive')

def closure(fds):
	closure = set(fds)

	all_attrs = (
		{attr for fd in fds for attr in fd.lhs}
		| {attr for fd in fds for attr in fd.rhs})

	all_attr_permutations = list(map(frozenset, itertools.permutations(all_attrs)))

	while True:
		original_len = len(closure)

		for fd1 in fds:
			for attr_set in all_attr_permutations:
				closure.add(augment(fd1, attr_set))

			for fd2 in fds:
				try:
					closure.add(transitive(fd1, fd2))
				except ValueError:
					pass

			closure |= set(reflexive(fd1.lhs, all_attr_permutations))
			closure |= set(reflexive(fd1.rhs, all_attr_permutations))

		if len(closure) == original_len:
			break

	return closure

if __name__ == '__main__':
	FD = FunctionalDependency
	print(', '.join(map(str, closure({
		FD('A', 'B'),
		FD('A', 'C'),
		FD('CG', 'H'),
		FD('CG', 'I'),
		FD('B', 'H')}))))
