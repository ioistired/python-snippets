#!/usr/bin/env python3

import flask

app = flask.Flask(__name__, template_folder='.')

@app.route('/')
def index():
	return flask.render_template('jinja_exported_names_test.html')

if __name__ == '__main__':
	app.run(debug=True)
