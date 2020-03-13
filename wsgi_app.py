def app(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain; charset=us-ascii')])
	yield b'Hello, '
	yield b'world!'
