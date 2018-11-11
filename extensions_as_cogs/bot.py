#!/usr/bin/env python3
# encoding: utf-8

import contextlib
import importlib
import inspect
import sys

import discord
from discord.ext import commands

class ModuleCogCommand(commands.Command):
	@property
	def cog_name(self):
		return getattr(inspect.getmodule(self.callback), '_cog_name_', None)

class ModuleCogBase(commands.Bot):
	def add_cog(self, module_name):
		module = importlib.import_module(module_name)

		try:
			name = module._cog_name_
		except AttributeError:
			del sys.modules[module_name]
			raise discord.ClientException('cog does not have a name')

		if name in self.cogs:
			return

		try:
			module.setup(self)
		except AttributeError:
			del sys.modules[module_name]
			raise discord.ClientException('cog does not have a setup function')


		with contextlib.suppress(AttributeError):
			self.add_check(module.__global_check)

		with contextlib.suppress(AttributeError):
			self.add_check(module.__global_check_once)

		members = inspect.getmembers(module)

		for name, member in members:
			# register commands the cog has
			if isinstance(member, commands.Command):
				if member.parent is None:
					self.add_command(member)
				continue

			# register event listeners the cog has
			if name.startswith('on_'):
				self.add_listener(member, name)

	def get_cog_commands(self, name):
		"""Gets a unique set of the cog's registered commands
		without aliases.

		If the cog is not found, an empty set is returned.

		Parameters
		------------
		name: str
			The name of the cog whose commands you are requesting.

		Returns
		---------
		Set[:class:`.Command`]
			A unique set of commands without aliases that belong
			to the cog.
		"""

		try:
			cog = self.cogs[name]
		except KeyError:
			return set()

		return {c for c in self.all_commands.values() if inspect.getmodule(c.callback) is cog}

	def remove_cog(self, name):
		"""Removes a cog from the bot.

		All registered commands and event listeners that the
		cog has registered will be removed as well.

		If no cog is found then this method has no effect.

		If the cog defines a special member function named ``__unload``
		then it is called when removal has completed. This function
		**cannot** be a coroutine. It must be a regular function.

		Parameters
		-----------
		name : str
			The name of the cog to remove.
		"""

		cog = self.cogs.pop(name, None)
		if cog is None:
			return

		members = inspect.getmembers(cog)
		for name, member in members:
			# remove commands the cog has
			if isinstance(member, Command):
				if member.parent is None:
					self.remove_command(member.name)
				continue

			# remove event listeners the cog has
			if name.startswith('on_'):
				self.remove_listener(member)

		with contextlib.suppress(AttributeError):
			self.remove_check(cog.__global_check)

		with contextlib.suppress(AttributeError):
			self.remove_check(cog.__global_check_once)

class MyBot(ModuleCogBase):
	def __init__(self):
		super().__init__(command_prefix=commands.when_mentioned)
		self.add_cog('test_cog')
		# override our add_cog stuff so jishaku can load normally
		# super(ModuleCogBase, self).load_extension('jishaku')

	async def on_ready(self):
		print('Logged in as', self.user, self.user.id)

bot = MyBot()

if __name__ == '__main__':
	import os

	bot.run(os.environ['discord_bot_token'])
