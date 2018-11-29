# big brain meme

def tuple_swap(a, i, j):
	a[i], a[j] = a[j], a[i]

def tmp_swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def xor_swap(a, i, j):
	a[i] ^= a[j]
	a[j] ^= a[i]
	a[i] ^= a[j]

def add_swap(a, i, j):
	a[i] += a[j]
	a[j] = a[i] - a[j]
	a[i] -= a[j]
