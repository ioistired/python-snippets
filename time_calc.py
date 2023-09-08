#!/usr/bin/env python3
# encoding: utf-8

"""
my attempt at doing a four-function time calculator

maybe use the datetime module instead
"""

__all__ = ['Time']

from datetime import datetime
from numbers import Integral, Real

from simple_rstrip import rstrip

class Time:
	"""represents either:
		- an absolute time of day, such as 23:34:03, or
		- a duration of time, such as 23 hours, 34 minutes, and 3 seconds
	"""

	__slots__ = ('_days', '_hours', '_minutes', '_seconds')

	def __new__(cls, hours: Integral = 0, minutes: Integral = 0, seconds: Real = 0, *, days: Integral = 0):
		self = super().__new__(cls)

		self._days = days
		self._hours = hours
		self._minutes = minutes
		self._seconds = seconds

		return self

	@classmethod
	def from_seconds(cls, seconds: Real):
		minutes, seconds = divmod(seconds, 60)
		hours, minutes = divmod(minutes, 60)
		days, hours = divmod(hours, 24)
		return cls(int(hours), int(minutes), seconds, days=int(days))

	@classmethod
	def now(cls):
		now = datetime.now()
		return cls(now.hour, now.minute, now.second)

	def total_seconds(self) -> Real:
		return 60**2 * (self.hours + 24 * self.days) + 60 * self.minutes + self.seconds

	def __float__(self):
		return float(self.total_seconds())

	def normalize(self):
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

	def __mul__(self, other: Real):
		"""implements self * other"""
		return self.from_seconds(self.total_seconds() * other)

	def __truediv__(self, other: Real):
		return self.from_seconds(self.total_seconds() / other)

	def __floordiv__(self, other: Real):
		return self.from_seconds(self.total_seconds() // other)

	def __repr__(self):
		t = self.normalize()

		# Time(5, 4, 0) -> Time(5, 4)
		# Time(0, 0, 0) -> Time()
		no_trailing_zeros = rstrip((0).__eq__, [t.hours, t.minutes, t.seconds])
		kwargs = ''
		if t.days:
			kwargs = f'days={t.days!r}'

		pos_args = ', '.join(map(repr, no_trailing_zeros))
		if not pos_args or not kwargs:
			args = pos_args or kwargs
		else:
			args = f'{pos_args}, {kwargs}'
		return f'{type(self).__qualname__}({args})'

	def __str__(self):
		seconds = float(self.seconds)  # allow zero padding even if seconds is a Fraction
		s = '{0.hours}:{0.minutes:02}:{seconds:04}'.format(self.normalize(), seconds=seconds)
		if self.days:
			return f'{self.days}d {s}'
		return s

	def __hash__(self):
		t = self.normalize()
		return hash((t.days, t.hours, t.minutes, t.seconds))

	for attr_name in __slots__:
		def prop(self, name=attr_name):
			return getattr(self, name)
		public_name = attr_name.lstrip('_')
		prop.__name__ = public_name
		vars()[public_name] = property(prop)

	del attr_name, public_name, prop
