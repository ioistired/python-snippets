#!/usr/bin/env python3

import contextvars
import inspect

import asyncpg

connection = contextvars.ContextVar('connection')

# please deduplicate this decorator as much as possible
# rules: you may use the entire stdlib from 3.7+ and even third party modules
# (although my solution uses no additional imports)
#
# you should ideally deduplicate the two async for loops and the two `return await func(...)`s as well,
# though this is not strictly necessary (my solution does)
#
# don't worry about the rest of the code, just make sure the output and behavior are the same when you run this file

def wrap(func):
	if inspect.isasyncgenfunction(func):
		async def inner(*args, **kwargs):
			try:
				connection.get().is_closed()
			except (asyncpg.InterfaceError, LookupError):
				async with pool.acquire() as conn:
					connection.set(conn)
					async for x in func(*args, **kwargs):
						yield x
			else:
				async for x in func(*args, **kwargs):
					yield x
	else:
		async def inner(*args, **kwargs):
			try:
				connection.get().is_closed()
			except (asyncpg.InterfaceError, LookupError):
				async with pool.acquire() as conn:
					connection.set(conn)
					return await func(*args, **kwargs)
			else:
				return await func(*args, **kwargs)

	return inner

@wrap
async def gen(a, b):
	print("gen")
	print(" ", a, b)
	async with connection.get().transaction():
		async for a, b in connection.get().cursor('VALUES (1, 2), (3, 4)'):
			yield a, b

@wrap
async def func(a, b):
	print("func")
	print(" ", a, b)
	return await connection.get().fetchval('SELECT 1')

@wrap
async def both(a, b):
	print("both")
	print(" ", a, b)
	async for x in gen(a, b):
		pass

	await func(a, b)

async def main():
	import sys
	global pool
	try:
		pool = await asyncpg.create_pool(sys.argv[1])
	except IndexError:
		print('Usage:', sys.argv[0], '<asyncpg connection URL>', file=sys.stderr)
		sys.exit(0)  # no args were provided, so give help

	async for x in gen(1, 2):
		pass

	conn = connection.get()

	await func(3, 4)

	assert connection.get() is not conn

	async with pool.acquire() as conn:
		connection.set(conn)
		await func(5, 6)
		assert connection.get() is conn
		await func(7, 8)
		assert connection.get() is conn

	await both(9, 10)

	assert connection.get() is not conn

if __name__ == "__main__":
	import asyncio
	asyncio.run(main())
