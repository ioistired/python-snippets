from __future__ import print_function  # test on both versions

"""
a test to see whether name mangling still works if the resulting name is greater than 255 characters.
If the transformed name is extremely long
(longer than 255 characters), implementation defined truncation may
happen. If the class name consists only of underscores, no
transformation is done.
"""

VAR_NAME = 'a'
mangling_overhead = lambda var_name_length: var_name_length + 3

def test_mangling(var_name=VAR_NAME):
	for exponent in range(8, 100):
		power = 2**exponent - mangling_overhead(len(var_name))
		print('Testing a class with a name', power, 'chars big')
		cls = get_class(power, var_name)
		x = cls()
		if mangle(cls.__name__, var_name) not in dir(x):
			print(power, 'is too big!')
			return
	print('CPython too stronk')


def get_class(name_length, var_name=VAR_NAME):
	class_name = 'A' * name_length
	code = (
		'class %s:\n'
		'	__%s = 0')
	exec(code % (class_name, var_name))
	return locals()[class_name]


def mangle(class_name, var_name):
	return '_%s__%s' % (class_name, var_name)


if __name__ == '__main__':
	test_mangling()
