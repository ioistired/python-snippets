#!/usr/bin/env python3

import datetime

c = [0, 0]
d = datetime.date(2019,1,1)
while d.year != 2020:
	c[d.day % 2] += 1
	d += datetime.timedelta(days=1)
print(c)
