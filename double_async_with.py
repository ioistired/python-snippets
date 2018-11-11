#!/usr/bin/env python3
# encoding: utf-8

from contextlib import asynccontextmanager as acm

@acm
async def a():
	try:
		print(1)
		yield a
	finally:
		print(3)

@acm
async def b():
	try:
		print(4)
		yield 5
	finally:
		print(6)

async def main():
	async with a() as c, c():
		print(c)

if __name__ == '__main__':
	import asyncio
	asyncio.run(main())
