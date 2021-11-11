from thistlethwaite.constants import adjacentMask,strToMove,U,D,F,B,L,R
from thistlethwaite.goals import G1_G2,G2_G3
from thistlethwaite.utils import rotl,rotr,getEdge

class cubeState:
	def __init__(self, state, path=None):
		self.state = state
		self.path = path or []

	def shuffle(self, shuffle):
		for strMove in shuffle.split():
			self.state = self.move(strToMove[strMove]).state

	# ...
	def phase(self, phase):
		if phase == 0:
			return tuple(getEdge(self))
		elif phase == 1:
			return G1_G2(self)
		elif phase == 2:
			return G2_G3(self)
		else:
			return tuple(self.state)

	# ...
	def getByte(self, face, byte):
		return (self.state[face] >> 4 * byte) & 0xF

	# ... 
	def move(self, move):
		face = int(move / 3)  # number btw 0 and 5 included => get the face F/B/...
		rot = move % 3 + 1 # number btw 1 and 3 => clockwise/half/counterclockwise
		
		newState = self.state[:]
		for i in range(rot):
			#current face
			newState[face] = rotl(newState[face], 8)

			#adjacent face
			mask = adjacentMask[face]
			if face == 0: #for U
				tmp = newState[F] & mask
				newState[F] = (newState[F] & ~mask) | (newState[R] & mask)
				newState[R] = (newState[R] & ~mask) | (newState[B] & mask)
				newState[B] = (newState[B] & ~mask) | (newState[L] & mask)
				newState[L] = (newState[L] & ~mask) | tmp
			if face == 1: #for D
				tmp = newState[F] & mask
				newState[F] = (newState[F] & ~mask) | (newState[L] & mask)
				newState[L] = (newState[L] & ~mask) | (newState[B] & mask)
				newState[B] = (newState[B] & ~mask) | (newState[R] & mask)
				newState[R] = (newState[R] & ~mask) | tmp
			if face == 2: #for F
				tmp = newState[U] & mask
				newState[U] = (newState[U] & ~mask) | rotl(newState[L] & (mask := rotr(mask, 8)), 8)
				newState[L] = (newState[L] & ~mask) | rotl(newState[D] & (mask := rotr(mask, 8)), 8)
				newState[D] = (newState[D] & ~mask) | rotl(newState[R] & (mask := rotr(mask, 8)), 8)
				newState[R] = (newState[R] & ~mask) | rotl(tmp, 8)
			if face == 3: #for B
				tmp = newState[U] & mask
				newState[U] = (newState[U] & ~mask) | rotr(newState[R] & (mask := rotl(mask, 8)), 8)
				newState[R] = (newState[R] & ~mask) | rotr(newState[D] & (mask := rotl(mask, 8)), 8)
				newState[D] = (newState[D] & ~mask) | rotr(newState[L] & (mask := rotl(mask, 8)), 8)
				newState[L] = (newState[L] & ~mask) | rotr(tmp, 8)
			if face == 4: #for L
				tmp = newState[U] & mask
				newState[U] = (newState[U] & ~mask) | rotl(newState[B] & rotl(mask, 16), 16)
				newState[B] = (newState[B] & ~rotl(mask, 16)) | rotl(newState[D] & mask, 16)
				newState[D] = (newState[D] & ~mask) | (newState[F] & mask)
				newState[F] = (newState[F] & ~mask) | tmp
			if face == 5: #for R
				tmp = newState[U] & mask
				newState[U] = (newState[U] & ~mask) | (newState[F] & mask)
				newState[F] = (newState[F] & ~mask) | (newState[D] & mask)
				newState[D] = (newState[D] & ~mask) | rotl(newState[B] & rotl(mask, 16), 16)
				newState[B] = (newState[B] & ~rotl(mask, 16)) | rotl(tmp, 16)
		return cubeState(newState, self.path+[move])
