#!/usr/bin/env python3
# encoding: utf-8

import contextlib
import sqlite3
import time
import typing

import requests

session = requests.Session()

connection = sqlite3.connect('data/dad-jokes.db')

with contextlib.closing(connection.cursor()) as cursor:
	cursor.execute('CREATE TABLE IF NOT EXISTS jokes (id TEXT PRIMARY KEY, joke TEXT)')
	connection.commit()

def save_jokes(jokes: typing.Iterable[typing.Tuple[str, str]]):
	"""insert jokes.

	Jokes are a tuple of:

	id: the id from the API
	joke: the text of the joke
	"""
	with contextlib.closing(connection.cursor()) as cursor:
		cursor.executemany('INSERT OR IGNORE INTO jokes VALUES (?, ?)', jokes)
		connection.commit()

def get_jokes(page=1):
	result = session.get(
		'https://icanhazdadjoke.com/search',
		headers={'Accept': 'application/json'},
		params={'page': page, 'limit': 30},
	).json()

	done = result['current_page'] == result['next_page']

	return result['next_page'], tuple((row['id'], row['joke']) for row in result['results']), done

if __name__ == '__main__':
	import sys

	page = 0
	while True:
		page, jokes, done = get_jokes(page)

		print('Retrieved', len(jokes), 'jokes', file=sys.stderr, end='. ')
		print('Last joke id:', jokes[-1][0], file=sys.stderr)
		save_jokes(jokes)

		if done:
			print('Retrieved all jokes. Page:', page, file=sys.stderr)
			sys.exit(0)

		time.sleep(3)

	session.close()
	connection.close()
