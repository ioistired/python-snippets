#!/usr/bin/env python3
# encoding: utf-8

import asyncio

import aiocontextvars

x = aiocontextvars.ContextVar('x')
x.set(0)

loop = asyncio.get_event_loop()
aiocontextvars.enable_inherit(loop)

async def a():
	print(x.get())
	x.set('a')
	await asyncio.sleep(0)
	print(x.get())

async def b():
	x.set('b')
	await asyncio.sleep(0)
	print(x.get())

loop.create_task(a())
loop.run_until_complete(b())

# is the output 0 b a ?

# no, it was 0 a b
