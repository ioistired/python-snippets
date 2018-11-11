# first step is to genericize this function for unit testing
# we do this by replacing every condition of an if block with a parameter
# assumption: original if conditions have no side effects

import inspect
import itertools

def coerce_bool(f):
	def wrapper(*args, **kwargs):
		return bool(f(*args, **kwargs))
	return wrapper

@coerce_bool
def old_guard(A,B,C,D,E,F,G):
	"""return a falsy value (None) if checks fail, otherwise return True
	this is the "control" for the experiment"""
	# Ignore A without a heavy check on each invocation
	# this kills it right at the function call
	if A:
		return

	for _ in range(1):
		if B:
			break
		if C:
			if D:
				break
			if E:
				return
			if F:
				return
		if G:
			return

	# this is the guarded code
	# it is assumed at this point that the checks passed
	return True

def new_guard(A,B,C,D,E,F,G):
	"""return a falsy value if checks fail, otherwise return True"""
	if A:
		return False
	if B:
		return True
	if C:
		c_check = _check_if_c(D,E,F)
		if c_check is not None:
			return c_check
	if G:
		return False

	# checks pass
	return True

def _check_if_c(D,E,F):
	if D:
		return True
	if E:
		return False
	if F:
		return False

	# C specific checks passed
	return None


def all_conditions(num_checks):
	return itertools.product((False, True), repeat=num_checks)

def arg_count(f):
	return len(inspect.signature(f).parameters)

def test():
	import inspect

	num_args = arg_count(new_guard)
	for conditions in all_conditions(num_args):
		print(conditions)
		assert old_guard(*conditions) == new_guard(*conditions)
