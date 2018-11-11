import sys

def python(x):
	if x is not python:
		return
	class A:
		def __getitem__(self, x):
			if x is not python:
				return
			class B:
				def __getattr__(self, x):
					if x != 'python':
						return
					def c(x):
						if x is c:  # after assignment, python = c
							print('hello world')
					return c
			return B()
	return A()

sys.modules[__name__] = python
