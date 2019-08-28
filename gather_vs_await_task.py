#!/usr/bin/env python3

import asyncio
import traceback

test_cases = ((0.5, None), (1, Exception), (2, None))

async def sleep_then_raise(caller, delay, exc=None):
	await asyncio.sleep(delay)
	if exc is not None:
		raise exc
	print(caller, (delay, exc))

async def sync_using_gather():
	coros = [sleep_then_raise('sync_using_gather', delay, exc) for delay, exc in test_cases]
	await asyncio.gather(*coros)

async def sync_using_await_task():
	tasks = [asyncio.create_task(sleep_then_raise('sync_using_await_task', delay, exc)) for delay, exc in test_cases]
	for task in tasks:
		await task

async def main():
	for func in sync_using_gather, sync_using_await_task:
		print(func.__name__)
		print('─' * len(func.__name__))
		try:
			await func()
		except Exception:
			traceback.print_exc()

	for task in asyncio.all_tasks():
		if not task.done() and task != asyncio.current_task():
			await task

if __name__ == '__main__':
	asyncio.run(main())
