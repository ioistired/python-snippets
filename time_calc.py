#!/usr/bin/env python3
# encoding: utf-8

"""
my attempt at doing a four-function time calculator

maybe use the datetime module instead
"""

import more_itertools as _more_itertools
from numbers import Integral as _Integral, Real as _Real
import operator as _operator

class Time:
	__slots__ = ('_hours', '_minutes', '_seconds')

	def __new__(cls, hours: int, minutes: _Integral = 0, seconds: float = 0):
		self = super().__new__(cls)
		self._hours = hours
		self._minutes = minutes
		self._seconds = seconds

		return self

	@classmethod
	def from_seconds(cls, seconds: _Real):
		minutes, seconds = divmod(seconds, 60)
		hours, minutes = divmod(minutes, 60)
		return cls(int(hours), int(minutes), seconds)

	def total_seconds(self) -> _Real:
		return 60**2 * self.hours + 60 * self.minutes + self.seconds

	def __float__(self):
		return float(self.total_seconds())

	def  normalize(self):
		"""return a copy of self where minutes and seconds do not exceed 59

		leap seconds are NOT ALLOWED :<
		"""
		return self.from_seconds(self.total_seconds())

	def __sub__(self, other: 'Time'):
		"""implements self - other"""
		# subtraction and addition require that *other* be typed
		# because 5:03:02 - 3 is undefined (3 seconds, minutes, or hours?)
		return self.from_seconds(self.total_seconds() - other.total_seconds())

	def __add__(self, other: 'Time'):
		"""implements self + other"""
		return self.from_seconds(self.total_seconds() + other.total_seconds())

	def __mul__(self, other: _Real):
		"""implements self * other"""
		return self.from_seconds(self.total_seconds() * other)

	def __truediv__(self, other: _Real):
		return self.from_seconds(self.total_seconds() / other)

	def __floordiv__(self, other: _Real):
		return self.from_seconds(self.total_seconds() // other)

	def __repr__(self):
		t = self.normalize()
		no_trailing_zeroes = _more_itertools.rstrip((t.hours, t.minutes, t.seconds), _operator.not_)
		args = ', '.join(map(repr, no_trailing_zeroes))
		return f'{type(self).__qualname__}({args})'

	def __str__(self):
		seconds = float(self.seconds)  # allow zero padding even if seconds is a Fraction
		return '{0.hours}:{0.minutes:02}:{seconds:04}'.format(self.normalize(), seconds=seconds)

	def __hash__(self):
		t = self.normalize()
		return hash((t.hours, t.minutes, t.seconds))

	@property
	def hours(self):
		return self._hours

	@property
	def minutes(self):
		return self._minutes

	@property
	def seconds(self):
		return self._seconds
