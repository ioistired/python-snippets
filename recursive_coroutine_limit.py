#!/usr/bin/env python3
# encoding: utf-8

import asyncio
import sys


def recur_n_times(n):  # control
	if n == 0:
		return
	recur_n_times(n-1)


async def async_recur_n_times(n):  # intervention
	if n == 0:
		return
	await async_recur_n_times(n-1)


async def main():
	# goal is to answer the question: does the recursion limit apply to coroutines?
	rec_limit = sys.getrecursionlimit()-10
	print('Recursion limit:', rec_limit)
	print('Recurring a routine')
	recur_n_times(rec_limit)
	print('Recurring a coroutine as a generator')

	try:
		async_recur_n_times(rec_limit).send(None)
	except StopIteration:
		pass

	print('Recurring a coroutine using await')
	await async_recur_n_times(rec_limit)


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
