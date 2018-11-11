#!/usr/bin/env python3
# encoding: utf-8

def _subclasses(cls):
	try:
		return cls.__subclasses__()
	except TypeError:
		return type.__subclasses__(cls)

class _SubclassNode:
	__slots__ = frozenset(('cls', 'children'))

	def __init__(self, cls, children=None):
		self.cls = cls
		self.children = children or []

	def __repr__(self):
		if not self.children:
			return repr(self.cls)

		return '<{0.__class__.__qualname__} {0.cls} {0.children}>'.format(self)

def subclasses(cls, root=None):
	root = root or _SubclassNode(cls)

	root.children.extend(map(_SubclassNode, _subclasses(cls)))
	for child in root.children:
		subclasses(child.cls, child)

	return root

if __name__ == '__main__':
	class A: pass
	class B(A): pass
	class C(A): pass
	class D(B, C): pass
	class E(A): pass

	print(subclasses(A))
