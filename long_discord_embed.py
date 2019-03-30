#!/usr/bin/env python3
# encoding: utf-8

import discord

zwsp = '\N{zero width space}'
zwspnl = zwsp + '\n'
e = discord.Embed(description=zwspnl*1024)

for _ in range(3):
	e.add_field(name=zwsp, value=zwspnl*512)

e.add_field(name=zwsp, value=zwspnl*439)

print(len(e))

# just for fun, let's obfuscate it
# this version just uses lambdas for local variables, and unrolls the loop

print(len(lambda zwsp, zwspnl:
	discord.Embed(description=zwspnl*1024)
	.add_field(name=zwsp, value=zwspnl*512)
	.add_field(name=zwsp, value=zwspnl*512)
	.add_field(name=zwsp, value=zwspnl*512)
	.add_field(name=zwsp, value=zwspnl*439)
)(*(lambda zwsp: (zwsp, zwsp+'\n'))('\N{zero width space}')))

# this one uses anonymous recursion to implement the original loop

print((lambda zwsp, zwspnl:
	(lambda f: lambda *args: f(f)(*args))( # fix-point comb
		# i = 0; while i < 3: e.add_field(...512)
		# e.add_field(...439)
		(lambda f: lambda e, i:
			e.add_field(name=zwsp, value=zwspnl*439)
			if i == 3 else
			f(f)(e.add_field(name=zwsp, value=zwspnl*512), i + 1)))
	(discord.Embed(description=zwspnl*1024), 0)  # i = 0
)(*(lambda zwsp: (zwsp, zwsp+'\n'))('\N{zero width space}')))

# inefficient and dumb, but fun to write
