#!/usr/bin/env python3
# encoding: utf-8

import contextlib

async def raise_(x):
	raise x

async def main():
	with contextlib.supress(IndexError):
		await raise_(IndexError)  # does await work here?

main().send(None)
