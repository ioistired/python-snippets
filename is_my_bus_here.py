#!/usr/bin/env python3

import requests

import sys
import os

try:
	params = dict(key=os.environ['CTA_KEY'], stpid=sys.argv[1], format='json')
except IndexError:
	print('usage: <stop ID> [route number]')
	sys.exit(1)

if len(sys.argv) > 2:
	params['rt'] = sys.argv[2]

data = requests.get('http://www.ctabustracker.com/bustime/api/v2/getpredictions', params=params).json()
try:
	print(any(prediction['prdctdn'] == 'DUE' for prediction in data['bustime-response']['prd']))
except KeyError:
	print(data, file=sys.stderr)
	sys.exit(2)

