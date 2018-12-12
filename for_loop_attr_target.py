#!/usr/bin/env python3
# encoding: utf-8

class NoisySetattr:
	def __setattr__(self, name, value):
		print(f'self.{name} = {value}')

for i, NoisySetattr().x in enumerate('hello'):
	pass
