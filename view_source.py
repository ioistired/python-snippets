#!/usr/bin/env python3
# encoding: utf-8

from flask import Flask, request, Response
import requests


app = Flask(__name__)
session = requests.Session()


@app.route('/view-source:<path:url>')
def fetch(url):
	return Response(session.get(url).text, mimetype='text/plain')


if __name__ == '__main__':
	app.run()
