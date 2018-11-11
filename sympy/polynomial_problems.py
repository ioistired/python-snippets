import random

import sympy

symbol_x = sympy.Symbol('x')

def bell_rand(bound):
	return round(random.normalvariate(0, 0.05) * bound)

def polynom(coefficients, exponents):
	return sum(coefficient * symbol_x ** exponent for coefficient, exponent in zip(coefficients, exponents))

def random_polynom():
	terms = random.randrange(1, 11)
	coeffs = [bell_rand(1000) for _ in range(terms)]
	exponents = [bell_rand(10) for _ in range(terms)]

	return polynom(coeffs, exponents)

def random_derivative_truth():
	op = random.choice((sympy.Integral, sympy.Derivative))

	polynom = random_polynom()
	lhs = op(polynom)
	rhs = lhs.doit()

	sympy.Eq(lhs, rhs.simplify())
