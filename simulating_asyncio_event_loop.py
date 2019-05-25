#!/usr/bin/env python3

import asyncio

async def foo():
	# has to be non-zero in order to actually yield a Future
	x = await asyncio.sleep(5)
	return x

def test():
	m = foo().__await__()
	fut = next(m)
	fut.set_result(10)
	try:
		next(m)
	except StopIteration as exc:
		assert exc.value == 10

if __name__ == '__main__':
	test()
