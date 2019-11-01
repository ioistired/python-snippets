#!/usr/bin/env python3

import jinja2

jinja_env = jinja2.Environment(loader=jinja2.PackageLoader('foo.bar', 'templates'))
print(jinja_env.get_template('test.html').render())
