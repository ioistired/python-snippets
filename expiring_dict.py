import reprlib
import time

class ExpiringDict(dict):
	def __init__(self, *args, **kwargs):
		for k, v in dict(*args, **kwargs).items():
			self[k] = v

	def __getitem__(self, k):
		v, expiry = super().__getitem__(k)
		if expiry is None or expiry > time.monotonic():
			return v

		super().__delitem__(k)
		raise KeyError(k)

	def __setitem__(self, k, v):
		v, expiry = v
		expiry = expiry and expiry + time.monotonic()
		super().__setitem__(k, [v, expiry])

	def expire(self, k, seconds):
		self[k][1] = seconds + time.monotonic()

	def __delitem__(self, k):
		self[k]  # ensure that deleting an expired entry raises
		self.pop(k, None)  # it may have been deleted by getitem already so ignore KeyErrors

	@reprlib.recursive_repr()
	def __repr__(self):
		now = time.monotonic()
		return '{}({})'.format(type(self).__qualname__, ', '.join(
			f'{k!r}: ({v!r}, {expiry and max(expiry - now, 0)!r})'
			for k, (v, expiry) in self.items()))
