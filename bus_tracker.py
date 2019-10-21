#!/usr/bin/env python3

import sys
import os
from collections import defaultdict

from bot_bin.misc import natural_join
import requests

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

route_predictions = defaultdict(list)

for prediction in data['prd']:
	route_predictions[prediction['rt']].append(prediction['prdctdn'])

for route, predictions in route_predictions.items():
	print(f'{route}: {natural_join(predictions)} minutes')
