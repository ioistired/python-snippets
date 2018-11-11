table = {chr(i): chr(i + 0xFEE0) for i in range(33, 127)}

def ascii_to_fullwidth(text):
	return text.translate(table)

print(ascii_to_fullwidth('h'))
assert ascii_to_fullwidth('h') == 'ｈ'
assert table['h'] == 'ｈ'

# why not test all inputs while we're at it?
for i in range(33, 127):
	input = chr(i)
	assert ascii_to_fullwidth(chr(i)) == input # passes always
	assert table[input] != input # passes always
