import random

import sympy

symbol_x = sympy.Symbol('x')

def bell_rand(bound):
	return round(random.normalvariate(0, 0.05) * bound)

def random_maybe_trig_problem():
	a, b, c, d, e, f = map(lambda _: bell_rand(100), range(6))

	return sympy.Integral(
		a*sympy.E**(b*symbol_x) /
			(c*sympy.sqrt(d+e*sympy.E**(f*symbol_x))),
		symbol_x)

def random_maybe_trig_truth():
	I = random_trig_sub_problem()
	return sympy.Eq(I, I.simplify().doit())
