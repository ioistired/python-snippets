#!/usr/bin/env python3
# encoding: utf-8

# By @LyricLy
# Public Domain / CC-0 <https://creativecommons.org/publicdomain/zero/1.0/>

import time

from collections import defaultdict

class Entity:
	def __init__(self, value):
		self.value = value
		self.pos = 0
		self.vel = value

	def move(self):
		self.pos += self.vel
		if self.pos <= 0:
			return self.value
		self.vel -= 1

def print_entities(edct):
	print("\n" * 100)
	for i in range(max(edct.keys()))[::-1]:
		try:
			print(edct[i][0].value)
		except IndexError:
			print("-")
	time.sleep(1)

def arrowsort(lst, output=None):
	rlst = []
	edct = defaultdict(list, {0: list(map(Entity, lst))})
	while True:
		if output is not None:
			output(edct)
		new_edct = defaultdict(list)
		for n in edct:
			for x in edct[n]:
				r = x.move()
				if r is not None:
					rlst.append(r)
				else:
					new_edct[x.pos].append(x)
		if not new_edct:
			return rlst
		edct = new_edct

if __name__ == "__main__":
	xs = eval(input())
	arrowsort(xs, print_entities)
	print(xs)
