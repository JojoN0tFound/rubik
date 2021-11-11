import thistlethwaite.constants as const

INT_BITS = 32
INTEGER_MASK = (1 << INT_BITS) - 1

facenamesId = ["U", "D", "F", "B", "L", "R"]

# ...
def rotr(face, bits):
	return INTEGER_MASK & ((face << (INT_BITS - bits)) | (face >> bits))

# ...
def rotl(face, bits):
	return INTEGER_MASK & ((face << bits) | (face >> (INT_BITS - bits)))

#...
def moveToStr(move):
	result = facenamesId[int(move/3)]+{1: '', 2: '2', 3: "'"}[move%3+1]
	return result

# ...
def getEdgeOrientation(edge):
	if (edge[0] == const.ORANGE or edge[0] == const.RED):
		return 1

	if (edge[0] == const.GREEN or edge[0] == const.BLUE):
		if (edge[1] == const.WHITE or edge[1] == const.YELLOW):
			return 1

	return 0

# ...
def getCornerOrientation(corner):
	if (corner[0] == const.WHITE or corner[0] == const.YELLOW):
		return 0
	if (corner[1] == const.WHITE or corner[1] == const.YELLOW):
		return 1
	return 2

# ...
def getEdge(state, pos=0):
	if not pos:
		return ([
			getEdgeOrientation([state.getByte(const.UP, 5),state.getByte(const.FRONT, 1)]),
			getEdgeOrientation([state.getByte(const.UP, 3), state.getByte(const.RIGHT, 1)]),
			getEdgeOrientation([state.getByte(const.UP, 1), state.getByte(const.BACK, 1)]),
			getEdgeOrientation([state.getByte(const.UP, 7), state.getByte(const.LEFT, 1)]),
			getEdgeOrientation([state.getByte(const.DOWN, 1), state.getByte(const.FRONT, 5)]),
			getEdgeOrientation([state.getByte(const.DOWN, 3), state.getByte(const.RIGHT, 5)]),
			getEdgeOrientation([state.getByte(const.DOWN, 5), state.getByte(const.BACK, 5)]),
			getEdgeOrientation([state.getByte(const.DOWN, 7), state.getByte(const.LEFT, 5)]),
			getEdgeOrientation([state.getByte(const.FRONT, 3), state.getByte(const.RIGHT, 7)]),
			getEdgeOrientation([state.getByte(const.FRONT, 7), state.getByte(const.LEFT, 3)]),
			getEdgeOrientation([state.getByte(const.BACK, 7), state.getByte(const.RIGHT, 3)]),
			getEdgeOrientation([state.getByte(const.BACK, 3), state.getByte(const.LEFT, 7)])
		])
	else:
		return ([
			const.edge[(state.getByte(const.UP, 5), state.getByte(const.FRONT, 1))],
			const.edge[(state.getByte(const.UP, 3), state.getByte(const.RIGHT, 1))],
			const.edge[(state.getByte(const.UP, 1), state.getByte(const.BACK, 1))],
			const.edge[(state.getByte(const.UP, 7), state.getByte(const.LEFT, 1))],
			const.edge[(state.getByte(const.DOWN, 1), state.getByte(const.FRONT, 5))],
			const.edge[(state.getByte(const.DOWN, 3), state.getByte(const.RIGHT, 5))],
			const.edge[(state.getByte(const.DOWN, 5), state.getByte(const.BACK, 5))],
			const.edge[(state.getByte(const.DOWN, 7), state.getByte(const.LEFT, 5))],
			const.edge[(state.getByte(const.FRONT, 3), state.getByte(const.RIGHT, 7))],
			const.edge[(state.getByte(const.FRONT, 7), state.getByte(const.LEFT, 3))],
			const.edge[(state.getByte(const.BACK, 7), state.getByte(const.RIGHT, 3))],
			const.edge[(state.getByte(const.BACK, 3), state.getByte(const.LEFT, 7))]
		])

# ...
def getCorner(state, pos=0):
	if not pos:
		return ([
			getCornerOrientation([state.getByte(const.UP, 4), state.getByte(const.FRONT, 2), state.getByte(const.RIGHT, 0)]),
			getCornerOrientation([state.getByte(const.UP, 2), state.getByte(const.RIGHT, 2), state.getByte(const.BACK, 0)]),
			getCornerOrientation([state.getByte(const.UP, 0), state.getByte(const.BACK, 2), state.getByte(const.LEFT, 0)]),
			getCornerOrientation([state.getByte(const.UP, 6), state.getByte(const.LEFT, 2), state.getByte(const.FRONT, 0)]),
			getCornerOrientation([state.getByte(const.DOWN, 2), state.getByte(const.RIGHT, 6), state.getByte(const.FRONT, 4)]),
			getCornerOrientation([state.getByte(const.DOWN, 0), state.getByte(const.FRONT, 6), state.getByte(const.LEFT, 4)]),
			getCornerOrientation([state.getByte(const.DOWN, 6), state.getByte(const.LEFT, 6), state.getByte(const.BACK, 4)]),
			getCornerOrientation([state.getByte(const.DOWN, 4), state.getByte(const.BACK, 6), state.getByte(const.RIGHT, 4)])
		])
	else :
		return ([
			const.corner[frozenset([state.getByte(const.UP, 4), state.getByte(const.FRONT, 2), state.getByte(const.RIGHT, 0)])],
			const.corner[frozenset([state.getByte(const.UP, 2), state.getByte(const.RIGHT, 2), state.getByte(const.BACK, 0)])],
			const.corner[frozenset([state.getByte(const.UP, 0), state.getByte(const.BACK, 2), state.getByte(const.LEFT, 0)])],
			const.corner[frozenset([state.getByte(const.UP, 6), state.getByte(const.LEFT, 2), state.getByte(const.FRONT, 0)])],
			const.corner[frozenset([state.getByte(const.DOWN, 2), state.getByte(const.RIGHT, 6), state.getByte(const.FRONT, 4)])],
			const.corner[frozenset([state.getByte(const.DOWN, 0), state.getByte(const.FRONT, 6), state.getByte(const.LEFT, 4)])],
			const.corner[frozenset([state.getByte(const.DOWN, 6), state.getByte(const.LEFT, 6), state.getByte(const.BACK, 4)])],
			const.corner[frozenset([state.getByte(const.DOWN, 4), state.getByte(const.BACK, 6), state.getByte(const.RIGHT, 4)])]
		])
