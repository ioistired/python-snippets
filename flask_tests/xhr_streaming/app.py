#!/usr/bin/env python3

import time

from itertools import count
from flask import Flask

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/stream')
def stream():
	def gen():
		yield 'image-id: 1'
		for i in range(1, 17):
			time.sleep(0.5)
			yield f'design-id: {i}'

	return app.response_class(gen(), mimetype='text/plain')

if __name__ == '__main__':
	app.run()
