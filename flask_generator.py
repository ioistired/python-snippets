#!/usr/bin/env python3

import time

from flask import Flask, Response


app = Flask('generator')


# fails
# @app.route('/')
def gen():
	for i in range(10):
		yield str(i)
		time.sleep(i)

@app.route('/')
def gen():
	def gen():
		for i in range(10):
			yield '%s\n' % i
			time.sleep(1)  # simulate an expensive operation
	return Response(gen(), mimetype='text/plain')

if __name__ == '__main__':
	app.run(host='localhost', port=8000)
