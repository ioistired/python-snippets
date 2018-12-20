#!/usr/bin/env python3
# encoding: utf-8

import asyncio
import contextvars

x = contextvars.ContextVar('x')
x.set(0)

async def a():
	print(x.get())
	x.set('a')
	await asyncio.sleep(0)
	print(x.get())

async def b():
	x.set('b')
	await asyncio.sleep(0)
	print(x.get())

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.create_task(a())
	loop.run_until_complete(b())

# is the output 0 b a ?

# no, it was 0 a b
