mod = __import__('', globals=globals(), fromlist=('a'), level=2)
assert mod.x == 1
