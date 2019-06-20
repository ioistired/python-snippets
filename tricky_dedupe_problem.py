#!/usr/bin/env python3

import asyncio
import contextlib
import inspect

@contextlib.asynccontextmanager
async def pool():
	try:
		yield "connection"
	finally:
		print("the connection is now closed")

CONNECTION = None

def set_connection(connection):
	global CONNECTION
	CONNECTION = connection

def get_connection():
	return CONNECTION


# please deduplicate this decorator as much as possible
# rules: you may use the entire stdlib from 3.7 and even third party modules
# (although my solution doesn't require any additional imports than what's written)
#
# you should ideally deduplicate the two async for loops and the two `return await`s as well,
# though this is not strictly necessary (my solution does)
#
# don't worry about the rest of the code, just make sure the output is the same when you run this file
def wrap(func):
	if inspect.isasyncgenfunction(func):
		async def inner(*args, **kwargs):
			try:
				1/0
			except ZeroDivisionError:
				async with pool() as conn:
					set_connection(conn)
					async for x in func(*args, **kwargs):
						yield x
			else:
				async for x in func(*args, **kwargs):
					yield x
	else:
		async def inner(*args, **kwargs):
			try:
				1/0
			except ZeroDivisionError:
				async with pool() as conn:
					set_connection(conn)
					return await func(*args, **kwargs)
			else:
				return await func(*args, **kwargs)

	return inner

awaitable = lambda x: asyncio.sleep(0, x)

async def aiter(iterable):
	await asyncio.sleep(0)  # to make this into an async gen
	for x in iterable:
		yield x

@wrap
async def agen(a, b):
	print("agen")
	print(' ', a, b)
	print(' ', get_connection())
	async for i in aiter([awaitable("a"), awaitable("b")]):
		yield i

@wrap
async def acor(a, b):
	print("acor")
	print(" ", a, b)
	print(" ", get_connection())
	return await awaitable("blah")

async def main():
	async for x in agen(1, 2):
		pass

	await acor(1, 2)

if __name__ == '__main__':
	asyncio.run(main())
