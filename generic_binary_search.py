import typing

def binary_search(predicate: typing.Callable[[int], int], lo, hi):
	while lo < hi:
		mid = (lo + hi) // 2
		cmp = predicate(mid)
		if cmp < 0:  # x < mid
			hi = mid
			continue

		if cmp == 0:  # x == mid
			return mid

		# x > mid
		lo = mid + 1

	return -lo

def interactive_predicate(i):
	val = input(f'enter "-" if {i} is too low, "=" if {i} is correct, or "+" if {i} is too high: ')
	return {
		'-': 1,  # user said "i < x", so return "x > i"
		'=': 0,
		'+': -1,  # user said "i > x", so return "x < i"
	}[val]

if __name__ == '__main__':
	import sys

	lo = int(input('Low index? '))
	hi = int(input('High index? '))
	i = binary_search(interactive_predicate, lo, hi)
	if i < 0:
		print('index not found, but it should be near', -i)
		sys.exit(1)

	print('index found:', i)
	sys.exit(0)
