_pi = 884279719003555 / 281474976710656

def __getattr__(x):
	if x != 'pi':
		raise AttributeError

	global _pi
	ret = _pi
	_pi += 0.001
	return ret

