#!/usr/bin/env python3
# encoding: utf-8

import contextlib
import time
import sqlite3

import requests

session = requests.Session()

connection = sqlite3.connect('data/dad-jokes.db')

with contextlib.closing(connection.cursor()) as cursor:
	cursor.execute('CREATE TABLE IF NOT EXISTS joke (id TEXT, joke TEXT)')
	cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS joke_id_idx ON joke (id)')
	connection.commit()

def save_joke(id, joke) -> bool:
	"""insert a joke.
	id: the id from the API
	joke: the text of the joke

	returns: whether the joke is new
	"""
	# we're just doing one query here so we don't need a cursor
	try:
		connection.execute('INSERT INTO joke VALUES (?, ?)', (id, joke))
	except sqlite3.IntegrityError:
		return False
	else:
		return True

def get_joke():
	result = session.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'}).json()
	return result['id'], result['joke']

if __name__ == '__main__':
	import sys

	while True:
		id, joke = get_joke()
		print('Got', 'new' if save_joke(id, joke) else 'old', 'joke', file=sys.stderr)
		time.sleep(10)
