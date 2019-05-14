"""
sql bucket: put all your sql queries in a separate file and load them by name

inspired by this: https://github.com/cathugger/nksrv/blob/master/src/centpd/lib/sqlbucket/load.go
usage example: https://github.com/cathugger/nksrv/blob/master/aux/psqlib/web.sql
"""

from collections import defaultdict
import re

def load_bucket(fp):
	"""given a file-like object, read the queries delimited by `-- :name foo` comment lines
	return a dict mapping these names to their respective SQL queries
	the file-like is not closed afterwards.
	"""
	# tag -> list[lines]
	queries = defaultdict(list)
	current_tag = ''

	for line in fp:
		match = re.match('\s*--\s*:name\s*(\S+)\s*$', line)
		if match:
			current_tag = match[1]
			continue
		if current_tag:
			queries[current_tag].append(line)

	for tag, query in queries.items():
		queries[tag] = '\n'.join(query)

	return queries
