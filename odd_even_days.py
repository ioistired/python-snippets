#!/usr/bin/env python3

# created because a recent Everybody Votes Channel poll was
# "were you born on an odd or even day?" and I wanted to make the more likely prediction
# (falsely assuming birthdays are evenly distributed...)

import datetime

c = [0, 0]
d = datetime.date(2019,1,1)
while d.year != 2020:
	c[d.day % 2] += 1
	d += datetime.timedelta(days=1)
print(c)
