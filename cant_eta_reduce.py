#!/usr/bin/env python3
# encoding: utf-8

class Messageable:
	channel_id = 1

	def typing(self):
		return Typing(self)

class Typing:
	def __init__(self, messageable):
		self.channel_id = messageable.channel_id

assert Messageable().typing().channel_id == 1

class CustomTyping:
	def __init__(self, messageable):
		self.channel_id = messageable.channel_id + 1

Messageable.typing = CustomTyping

assert Messageable().typing().channel_id == 2

# the error in logic is thinking that typing(self) -> Typing(self)
# is the same as typing = Typing
# it's not.
#
# The self argument gets bound, so it's more like typing = lambda: Typing()
