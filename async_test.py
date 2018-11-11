#!/usr/bin/env python3
# encoding: utf-8


async def hello_world():
	return 'Hello, world!'


async def say_hi():
	print(await hello_world())
