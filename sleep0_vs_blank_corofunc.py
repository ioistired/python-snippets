#!/usr/bin/env python3
# encoding: utf-8

"""
(Probably unfair) micro benchmark of different ways of yielding to the event loop.

This benchmark seems to be unfair because (among other reasons) awaiting a coroutine function
that is not actually asynchronous, as corofunc_sleep0 is defined below, does not schedule other tasks.
Asyncio.sleep(0), on the other hand, does.

See the output of aio_interleaved_output_blank_corofunc.py in this repository for a demo of that behavior.
"""

import asyncio
import time
import types

async def timeit(f, _timer=time.perf_counter):
	t0 = _timer()
	for _ in range(1_000_000):
		await f(0)
	t1 = _timer()
	return t1 - t0

async def corofunc_sleep0(_):  # one parameter is defined for parity with asyncio.sleep
	pass

# this one relies on implementation details of asyncio, so even if it is the fastest,
# it's probably better not to use it
# see the definition of asyncio.tasks.__sleep0
@types.coroutine
def bare_yield_sleep0(_):
	yield

if __name__ == '__main__':
	loop = asyncio.get_event_loop()

	funcs = [asyncio.sleep, corofunc_sleep0, bare_yield_sleep0]
	times = {func: loop.run_until_complete(timeit(func)) for func in funcs}

	for func, time in times.items():
		print(func.__name__, '->', time)

	print('asyncio.sleep(0) is', times[asyncio.sleep]/times[corofunc_sleep0], 'slower than corofunc_sleep0')
