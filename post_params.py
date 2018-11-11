#!/usr/bin/env python3
# encoding: utf-8

import flask

app = flask.Flask(__name__)

@app.route('/test', methods=('POST', 'GET'))
def test():
	if flask.request.method == 'GET':
		return ('<form method="POST">\n'
			'<input type="number" name="num">\n'
			'<input type="submit">\n'
			'</form>')
	else:
		return '{}<br>{}'.format(flask.request.args, flask.request.form)


if __name__ == '__main__':
	app.run(port=5000)
