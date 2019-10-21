import asyncio

# SPDX-License-Identifier: Apache-2.0 OR BlueOak-1.0.0

async def gather_or_cancel(*awaitables, loop=None):
	futs = list(map(asyncio.create_task, awaitables))

	def cancel_children(_):
		for fut in futs:
			fut.cancel()

	g = asyncio.gather(*futs, loop=loop)
	g.add_done_callback(cancel_children)
	return await g

async def a():
	await asyncio.sleep(0.5)
	print('a')

async def b():
	await asyncio.sleep(1)
	raise ValueError

async def c():
	await asyncio.sleep(1.5)
	print('c')
	await asyncio.sleep(0)

async def main():
	await gather_or_cancel(a(), b(), c())

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.create_task(main())
	loop.run_forever()
