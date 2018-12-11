#!/usr/bin/env python3
# encoding: utf-8

from dataclasses import dataclass
import enum
import operator

"""
Construct a finite-state machine for a combination lock that:
	- contains numbers 1 through 40, and
	- opens only when the correct combination, 10 right, 8 second left, 37 right, is entered.

Each input is a triple consisting of:
	- a number,
	- the direction of the turn,
	- and the number of times the lock is turned in that direction.
"""

class CircularDirection(enum.IntEnum):
	counter_clockwise = -1
	clockwise = 1

@dataclass
class ComboLockInput:
	number: int
	direction: CircularDirection
	cycles: int

@dataclass
class ComboLockState:
	id: int
	needed_input: ComboLockInput
	next_state: int

class ComboLock:
	states = (
		# accepting and rejecting state
		ComboLockState(0, ComboLockInput(10, CircularDirection.clockwise, 1), 1),
		# during input of combo
		ComboLockState(1, ComboLockInput(8, CircularDirection.counter_clockwise, 2), 2),
		# waiting for end of combo
		ComboLockState(2, ComboLockInput(37, CircularDirection.clockwise, 1), 3),
	)

	state = states[0]

	def transition(self, input: ComboLockInput):
		if input == self.state.needed_input:
			self.state = self.next_state(input)
		else:
			# reject and go back to 0
			self.state = self.states[0]

	def next_state(self, input: ComboLockInput):
		next_index = (self.state.id + 1) % len(self.states)
		return self.states[next_index]
