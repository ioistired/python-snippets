#!/usr/bin/env python3
# encoding: utf-8

from flask import Flask, request, session, Response

app = Flask(__name__)
app.secret_key = '7a4c9vrTTNocioZmoli-VzJRV6DmQcLvS8xToKUZL-s'

@app.route('/')
def index():
	session.setdefault('foo', 'baz')
	return Response(session['foo'])

@app.route('/a')
def a():
	return Response('a')

if __name__ == '__main__':
	app.run(debug=True)
