#!/usr/bin/env python3
# encoding: utf-8

from collections import namedtuple

timedelta = namedtuple('timedelta', 'days hours minutes seconds')

def human_time(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return timedelta(days, hours, minutes, seconds)


if __name__ == '__main__':
	print(human_time(135951))
