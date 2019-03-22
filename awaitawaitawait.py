#!/usr/bin/env python3
# encoding: utf-8

import asyncio

async def f(*, n=5):
	if n == 1: return True
	return f(n=n-1)

async def main():
	print(await (await (await (await (await f())))))

asyncio.run(main())
