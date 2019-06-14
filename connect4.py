from io import StringIO

class Connect4:
	WIDTH = 7
	HEIGHT = 6

	H1 = HEIGHT + 1
	H2 = HEIGHT + 2
	SIZE = HEIGHT * WIDTH
	SIZE1 = H1 * WIDTH
	ALL1 = (1 << SIZE1) - 1
	COL1 = (1 << H1) - 1
	BOTTOM = ALL1 // COL1
	TOP = BOTTOM << HEIGHT

	def __init__(self):
		self.turns = 0
		self.lowest_free_squares = [self.H1 * i for i in range(self.WIDTH)]
		self.boards = [0, 0]

	reset = __init__

	def is_playable(self, col):
		"""return whether the column has room"""
		return self.is_legal(self.boards[self.plies & 1] | (1 << self.lowest_free_squares[col]))

	def is_legal(self, board):
		"""return whether the board lacks an overflowing column"""
		return self.boards[self.turns & 1] & TOP == 0

	def has_won(self, player):
		board = self.boards[player]
		y = board & (board >> self.HEIGHT)
		if (y & (y >> 2 * self.HEIGHT)) != 0:  # diagonal \
			return True
		y = board & (board >> self.H1)
		if (y & (y >> 2 * self.H1)) != 0:  # horizontal -
			return True
		y = board & (board >> self.H2)
		if (y & (y >> 2 * self.H2)) != 0:  # diagonal /
			return True
		y = board & (board >> 1)
		return (y & (y >> 2)) != 0  # vertical |

	def move(self, col):
		self.boards[self.turns & 1] |= 1 << self.lowest_free_squares[col]
		self.lowest_free_squares[col] += 1
		self.turns += 1

	def __getitem__(self, xy):
		x, y = xy
		i = x * self.H1 + y
		mask = 1 << i
		return 0 if self.boards[0] & mask != 0 else 1 if self.boards[1] & mask != 0 else -1

	def __str__(self):
		buf = StringIO()

		for w in range(self.WIDTH):
			# column indexes
			buf.write(' ')
			buf.write(str(w + 1))

		buf.write('\n')

		for h in range(self.HEIGHT-1, -1, -1):
			for w in range(h, self.SIZE1, self.H1):
				mask = 1 << w
				buf.write(
					' @' if self.boards[0] & mask != 0
					else ' 0' if self.boards[1] & mask != 0
					else ' .')
			buf.write('\n')

		if self.has_won(0):
			buf.write('\n@ won')
		if self.has_won(1):
			buf.write('\n0 won')

		return buf.getvalue()
