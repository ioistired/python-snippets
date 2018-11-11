#!/usr/bin/env python3
# encoding: utf-8

"""
my attempt at doing a four-function time calculator

maybe use the datetime module instead
"""


class Time:
	__slots__ = ('_hours', '_minutes', '_seconds')

	def __init__(self, hours, minutes=0, seconds=0):
		self._hours = hours
		self._minutes = minutes
		self._seconds = seconds

	@classmethod
	def from_seconds(cls, seconds: int):
		minutes, seconds = divmod(seconds, 60)
		hours, minutes = divmod(minutes, 60)
		return cls(hours, minutes, seconds)

	@property
	def total_seconds(self):
		return 60*60*self.hours + 60*self.minutes + self.seconds

	def __sub__(self, other):
		"""implements self - other (where other is another Time)"""
		# subtraction and addition require that *other* be typed
		# because 5:03:02 - 3 is undefined (3 seconds, minutes, or hours?)
		return self.from_seconds(self.total_seconds - other.total_seconds)

	def __add__(self, other):
		"""implements self + other (where other is another Time)"""
		return self.from_seconds(self.total_seconds + other.total_seconds)

	def __mul__(self, other: int):
		"""implements self * other"""
		return self.from_seconds(self.total_seconds * other)

	def __truediv__(self, other: int):
		return self.from_seconds(self.total_seconds / other)

	def __floordiv__(self, other: int):
		return self.from_seconds(self.total_seconds // other)

	def __repr__(self):
		# TODO strip trailing zero arguments from the repr
		# i.e. repr(Time(1,2,0)) -> "Time(1, 2)"
		return '{0.__class__.__name__}({0.hours}, {0.minutes}, {0.seconds})'.format(self)

	@property
	def hours(self):
		return self._hours

	@hours.setter
	def set_hours(self):
		raise TypeError('"hours" attribute is immutable')

	@hours.deleter
	def delete_hours(self):
		raise TypeError('"hours" attribute is immutable')

	@property
	def minutes(self):
		return self._minutes

	@minutes.setter
	def set_minutes(self):
		raise TypeError('"minutes" attribute is immutable')

	@minutes.deleter
	def delete_minutes(self):
		raise TypeError('"minutes" attribute is immutable')

	@property
	def seconds(self):
		return self._seconds

	@seconds.setter
	def set_seconds(self):
		raise TypeError('"seconds" attribute is immutable')

	@seconds.deleter
	def delete_seconds(self):
		raise TypeError('"seconds" attribute is immutable')
