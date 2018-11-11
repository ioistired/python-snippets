#!/usr/bin/env python3
# encoding: utf-8

import contextlib
import json
import sqlite3

connection = sqlite3.connect('data/dad-jokes.db')

with contextlib.closing(connection.cursor()) as cursor:
	cursor.execute('SELECT id, joke FROM jokes')
	jokes = dict(cursor.fetchall())

with open('data/dad-jokes.json', 'w') as f:
	json.dump(jokes, f, ensure_ascii=False, indent=2)

connection.close()
