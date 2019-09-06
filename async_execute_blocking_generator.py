#!/usr/bin/env python3

import asyncio
import functools

def foo():
	yield from range(3)

async def asyncgen(gen):
	for x in gen:
		await asyncio.sleep(0)
		yield x

async def gen_in_executor(gen, *, prime=True):
	loop = asyncio.get_event_loop()
	if prime: next(gen)
	while True:
		try:
			yield await loop.run_in_executor(None, next, gen)
		except StopIteration as exc:
			raise StopAsyncIteration(*exc.args)

async def main():
	async for x in asyncgen(foo()):
		print(x)

	async for x in gen_in_executor(foo()):
		print(x)

if __name__ == '__main__':
	asyncio.get_event_loop().run_until_complete(main())
