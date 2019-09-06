# this file demonstrates the primary motivating use case for "lua style configs"
d = {
	'foo': 1,
	'bar': {
		'baz': 3,
		'quux': 4,
	}
}
d['waldo'] = d['bar']
return d
