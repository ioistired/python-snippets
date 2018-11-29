def foo(
	w,
	x: int,
	y: 'SomeType',
	z: int = 0,
	*,
	a,
	b,
	c: tuple = None,
	**kwargs
):
	return (w, x, y, z), (a, b, kwargs)
