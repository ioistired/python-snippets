#!/usr/bin/env python3
# encoding: utf-8

class NoisySetattr:
	def __setattr__(self, name, value):
		print(f'self.{name} = {value}')

for NoisySetattr().x in 'hello':
	pass
