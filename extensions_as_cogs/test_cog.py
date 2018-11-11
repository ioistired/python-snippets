#!/usr/bin/env python3
# encoding: utf-8

from discord.ext import commands

_cog_name_ = 'Tests'

@commands.command()
async def ping(context):
	await context.send(f'Pong. Latency: {bot.latency:.2f}')

async def on_ready():
	print('Ready from test_cog')

def setup(passed_bot):
	global bot
	bot = passed_bot
