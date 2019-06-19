#!/usr/bin/env python3

import trio

async def a():
	print('enter a')
	await trio.sleep(0)
	print('leave a')

async def b():
	print('enter b')
	await trio.sleep(0)
	print('leave b')

async def main():
	async with trio.open_nursery() as nursery:
		print(nursery.start_soon(a))
		nursery.start_soon(b)

# seems like the output order is non-deterministic

if __name__ == '__main__':
	trio.run(main)
