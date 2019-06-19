#!/usr/bin/env python3

import trio

async def a():
	print('enter a')
	await trio.sleep(1)
	print('leave a')

async def b():
	print('enter b')
	await trio.sleep(0)
	print('leave b')

async def c():
	print('enter c')
	await trio.sleep(0)
	print('leave c')

async def d():
	print('enter d')
	await trio.sleep(0)
	print('leave d')

async def main():
	async with trio.open_nursery() as nursery:
		for f in a, b, c, d:
			nursery.start_soon(f)

if __name__ == '__main__':
	trio.run(main)
