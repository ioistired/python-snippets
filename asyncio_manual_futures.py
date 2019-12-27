#!/usr/bin/env python3

import asyncio

async def task_a(fut):
	await asyncio.sleep(0)
	fut.set_result(1)
	await asyncio.sleep(0)

async def task_b(fut):
	print(await fut)

async def amain():
	fut = asyncio.get_running_loop().create_future()
	await asyncio.gather(task_b(fut), task_a(fut), task_b(fut))

if __name__ == '__main__':
	asyncio.run(amain())
