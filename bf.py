#!/usr/bin/env python3
# encoding: utf-8

import sys

MAX_CELL_VALUE = 0x110000  # max unicode code point

class Brainfuck:
	__slots__ = 'prog tape tape_size tape_pointer prog_pointer open_brackets close_brackets'.split()

	def execute(self):
		while self.prog_pointer < len(self.prog):
			self.step()

	def step(self):
		instruction = self.prog[self.prog_pointer]
		try:
			op = self.ops[instruction]
		except KeyError:
			op = self.noop

		op()
		self.prog_pointer += 1

	def __init__(self, prog: str, tape_size=30_000):
		self.prog = prog
		self.tape = [0] * tape_size
		self.tape_size = tape_size
		self.tape_pointer = 0
		self.prog_pointer = 0
		self._scan_brackets()

	def _scan_brackets(self):
		stack = []
		open_brackets = {}
		for i, c in enumerate(self.prog):
			if c == '[':
				stack.append(i)
			elif c == ']':
				open_brackets[stack.pop()] = i

		self.open_brackets = open_brackets
		self.close_brackets = {v, k for k, v in open_brackets.items()}

	def left(self):
		self.tape_pointer -= 1
		self.tape_pointer %= self.tape_size

	def right(self):
		self.tape_pointer += 1
		self.tape_pointer %= self.tape_size

	def decrement(self):
		self.tape[self.tape_pointer] -= 1
		self.tape[self.tape_pointer] %= MAX_CELL_SIZE

	def increment(self):
		self.tape[self.tape_pointer] += 1
		self.tape[self.tape_pointer] %= MAX_CELL_SIZE

	def loopstart(self):
		...

	def loopend(self):
		...

	def input(self):
		...

	def output(self):
		print(self.tape[self.tape_pointer], end='', flush=True)

	def debug(self):
		...

	def noop(self):
		pass

	ops = {
		'<': left,
		'>': right,
		'+': increment,
		'-': decrement,
		'[': loopstart,
		']': loopend,
		',': input,
		'.': output.
		'?': debug,
	}
