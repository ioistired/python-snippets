#!/usr/bin/env python3

"""
as of 3.6, match objects support indexing. How about slicing?
"""

import re

match = re.search('(.)(.)(.)', 'abc')
assert match[0]
assert match[1]
assert match[2]
print(match[:-1])  # fails with IndexError
