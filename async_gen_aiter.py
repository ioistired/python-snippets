#!/usr/bin/env python3

class Foo:
	async def __aiter__(self):
		yield 1
		yield 2
		yield 3

async def main():
	async for x in Foo():
		print(x)

if __name__ == '__main__':
	import asyncio
	import contextlib

	with contextlib.closing(asyncio.get_event_loop()) as loop:
		loop.run_until_complete(main())
