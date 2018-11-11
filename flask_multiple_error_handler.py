#!/usr/bin/env python3
# encoding: utf-8

import flask
from werkzeug.exceptions import NotFound, InternalServerError

app = flask.Flask(__name__)


@app.route('/cats/<breed>')
def cats(breed):
	"""wonky code ahead!"""
	return


@app.errorhandler(404)
def not_found(e):
	# shame that i have to do it like this, instead of just returning
	# like e.status_code or smth
	if isinstance(e, NotFound):
		status_code = 404
	elif isinstance(e, InternalServerError):
		status_code = 500
	else:
		raise e

	return 'ya dun guffed ({})'.format(status_code), status_code


# looks like you have to separate them :(
@app.errorhandler(500)
def internal_server_error(e):
	return 'ya dun guffed ({})'.format(500)


if __name__ == '__main__':
	app.run()
