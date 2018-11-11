#!/usr/bin/env python3
# encoding: utf-8

# modelled after discord.ext.commands.bot.Bot
# c.f. https://github.com/Rapptz/discord.py/blob/871a262ee37aa09c557b8543f18fd699b940c07f/discord/ext/commands/bot.py

class Client:
	latency = 100.0

class BotBase:
	command_prefix = 1

class Bot(BotBase, Client):
	pass

class MyBot(Bot):
	def __init__(self):
		# AttributeError if both have __init__ and these are set in __init__
		print(super().command_prefix)
		print(super().latency)

if __name__ == '__main__':
	MyBot()
