#!/usr/bin/env python3
# encoding: utf-8

# access an iterable at a given index
# equivalent to list(it)[i] but doesnt iterate through the whole thing
# - assume the index is valid, ie do not handle StopIteration
# - no named recursion
const = lambda x: lambda y: x
discard = const(None)
tail = lambda it: discard(next(it)) or it
def raise_(x): raise x

igetitem_cheating = (lambda it, i:
	next(it)
	if i == 0
	else igetitem_cheating(tail(it), i-1))

# anonymous recursive version
igetitem = (lambda f: lambda *args: f(f)(*args))(lambda f:
	lambda it, i:
		next(it)
		if i == 0
		else f(f)(tail(it), i-1))

igetitem_inlined = (lambda f: lambda *args: f(f)(*args))(lambda f:
	lambda it, i:
		next(it)
		if i == 0
		else f(f)(
			(lambda it: (lambda _: None)(next(it)) or it)
				(it),
			i-1))

def test_impl(igetitem):
	range10_iter = lambda: iter(range(10))
	for i in range(10):
		assert igetitem(range10_iter(), i) == i

def test():
	for func in igetitem_cheating, igetitem, igetitem_inlined:
		test_impl(func)

if __name__ == '__main__':
	test()
