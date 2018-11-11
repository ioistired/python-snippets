from typing import Sequence

def power_set(xs: Sequence):
	if not xs:
		return ()
	return (power_set(xs[:-1]), xs[-1])
