#!/usr/bin/env python3

import datetime as dt
import functools
import sys
import os
from collections import defaultdict

import requests
from bot_bin.misc import natural_join

try:
	params = dict(key=os.environ['CTA_BUS_KEY'], stpid=sys.argv[1], format='json')
except IndexError:
	print('usage: <stop ID> [route number]')
	sys.exit(1)

if len(sys.argv) > 2:
	params['rt'] = sys.argv[2]

data = requests.get('http://www.ctabustracker.com/bustime/api/v2/getpredictions', params=params).json()\
	['bustime-response']

def err(*args, **kwargs):
	print(f'{sys.argv[0]}:', *args, file=sys.stderr, **kwargs)

if 'error' in data:
	for error in data['error']:
		err(error)
	sys.exit(2)

route_predictions = defaultdict(lambda: defaultdict(list))

parse_time = functools.partial(dt.datetime.strptime, '%Y%m%d %H:%M')

for prediction in data['prd']:
	if prediction['dly']:
		eta = (parse_time(prediction['prdtm']) - parse_time(prediction['tmstmp'])).total_seconds() / 60
		eta = f'DELAYED (scheduled in {eta} minutes)'
	else:
		eta = prediction['prdctdn']
	route_predictions[prediction['stpnm']][prediction['rt'], prediction['des']].append(eta)

first_line = True
for stop_name, routes in route_predictions.items():
	if not first_line: print()  # put a blank line before each stop
	print(stop_name)
	print('─' * len(stop_name))
	first_line = False

	for (route, dest), predictions in routes.items():
		print(f'{route} to {dest}: {natural_join(predictions)} minutes')
