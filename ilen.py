from collections import deque

def ilen_a(xs):
	d = deque(enumerate(xs, 1), maxlen=1)
	return d[0][0] if d else 0

def ilen_b(xs):
	len = 0
	for len, _ in enumerate(xs, 1):
		pass
	return len
