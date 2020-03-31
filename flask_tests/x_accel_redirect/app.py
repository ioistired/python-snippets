#!/usr/bin/env python3

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/foo.png')
def foo():
	resp = make_response('')
	resp.headers['Content-Type'] = 'image/png'
	resp.headers['X-Accel-Redirect'] = '/protected/foo.png'
	return resp
