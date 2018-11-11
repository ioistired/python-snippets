import functools

def longest_word(words: str):  # Problem 6
	def f(info, c):
		current_word, longest_word = info
		if c.isspace():
			return '', max(current_word, longest_word, key=len)
		return current_word+c, longest_word

	current_word, longest_word = functools.reduce(f, words, ('', ''))
	return longest_word

def longest_word_iterative(words: str):
	current_word = ''
	longest_word = ''

	for c in words:
		if c.isspace():
			longest_word = max(current_word, longest_word, key=len)
			current_word = ''
		else:
			current_word += c

	return longest_word

def longest_word_builtin(words: str):
	return max(words.split(), key=len)
