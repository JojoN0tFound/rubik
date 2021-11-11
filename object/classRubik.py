import constants
import copy
from parsing import parseMovement


class Rubik:
	def startShuffle(self, shuffle):
		for move in shuffle.split():
			if(parseMovement(move) is False):
				raise ValueError(constants.ERROR_MOVEMENT)
			if(move == "L"):
				self.moveLeft()
			if(move == "L'"):
				self.moveCounterLeft()
			if(move == "L2"):
				self.moveLeftHalf()
			if(move == "R"):
				self.moveRight()
			if(move == "R'"):
				self.moveCounterRight()
			if(move == "R2"):
				self.moveRightHalf()
			if(move == "F"):
				self.moveFront()
			if(move == "F'"):
				self.moveCounterFront()
			if(move == "F2"):
				self.moveFrontHalf()
			if(move == "B"):
				self.moveBack()
			if(move == "B'"):
				self.moveCounterBack()
			if(move == "B2"):
				self.moveBackHalf()
			if(move == "U"):
				self.moveUp()
			if(move == "U'"):
				self.moveCounterUp()
			if(move == "U2"):
				self.moveUpHalf()
			if(move == "D"):
				self.moveDown()
			if(move == "D'"):
				self.moveCounterDown()
			if(move == "D2"):
				self.moveDownHalf()

	def __init__(self, shuffle):
		self.solution = False

		self.left = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
		self.right = [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
		self.up = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
		self.down = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]
		self.front = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
		self.back = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]

		self.structure = {
			"L": self.left,
			"R": self.right,
			"U": self.up,
			"D": self.down,
			"F": self.front,
			"B": self.back
		}

		self.startShuffle(shuffle)

	def reset(self):
		self.left = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
		self.right = [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
		self.up = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
		self.down = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]
		self.front = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
		self.back = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]

	def moveLeft(self):
		# Move Other Faces
		tmp = copy.deepcopy(self.front)
		for y in range(0, 3):
			self.front[y][0] = self.up[y][0]
			self.up[y][0] = self.back[2 - y][2]
			self.back[2 - y][2] = self.down[y][0]
			self.down[y][0] = tmp[y][0]
		# Move Left Face Itself
		self._turnFaceItself('L')
		if(self.solution is not False):
			self.solution.append('L')

	def moveCounterLeft(self):
		# Move Other Faces
		tmp = copy.deepcopy(self.up)
		for y in range(0, 3):
			self.up[y][0] = self.front[y][0]
			self.front[y][0] = self.down[y][0]
			self.down[y][0] = self.back[2 - y][2]
			self.back[2 - y][2] = tmp[y][0]
		# Move Left Face Itself
		self._turnCounterFaceItself('L')
		if(self.solution is not False):
			self.solution.append('L\'')

	def moveLeftHalf(self):
		self.moveLeft()
		self.moveLeft()

	def moveRight(self):
		# Move Other Faces
		tmp = copy.deepcopy(self.up)
		for y in range(0, 3):
			self.up[y][2] = self.front[y][2]
			self.front[y][2] = self.down[y][2]
			self.down[y][2] = self.back[2 - y][0]
			self.back[2 - y][0] = tmp[y][2]
		# Move Right Face Itself
		self._turnFaceItself('R')
		if(self.solution is not False):
			self.solution.append('R')

	def moveCounterRight(self):
		# Move Other Faces
		tmp = copy.deepcopy(self.front)
		for y in range(0, 3):
			self.front[y][2] = self.up[y][2]
			self.up[y][2] = self.back[2 - y][0]
			self.back[2 - y][0] = self.down[y][2]
			self.down[y][2] = tmp[y][2]
		# Move Right Face Itself
		self._turnCounterFaceItself('R')
		if(self.solution is not False):
			self.solution.append('R\'')

	def moveRightHalf(self):
		self.moveRight()
		self.moveRight()

	def moveFront(self):
		# Move Other Faces
		tmp = copy.deepcopy(self.up)
		for n in range(0, 3):
			self.up[2][2 - n] = self.left[n][2]
			self.left[n][2] = self.down[0][n]
			self.down[0][n] = self.right[2 - n][0]
			self.right[2 - n][0] = tmp[2][2 - n]
		# Move Front Face Itself
		self._turnFaceItself('F')
		if(self.solution is not False):
			self.solution.append('F')

	def moveCounterFront(self):
		# Move Other Faces
		tmp = copy.deepcopy(self.up)
		for n in range(0, 3):
			self.up[2][n] = self.right[n][0]
			self.right[n][0] = self.down[0][2 - n]
			self.down[0][2 - n] = self.left[2 - n][2]
			self.left[2 - n][2] = tmp[2][n]
		# Move Front Face Itself
		self._turnCounterFaceItself('F')
		if(self.solution is not False):
			self.solution.append('F\'')

	def moveFrontHalf(self):
		self.moveFront()
		self.moveFront()

	def moveBack(self):
		# Move Other Faces
		tmp = copy.deepcopy(self.up)
		for n in range(0, 3):
			self.up[0][n] = self.right[n][2]
			self.right[n][2] = self.down[2][2 - n]
			self.down[2][2 - n] = self.left[2 - n][0]
			self.left[2 - n][0] = tmp[0][n]
		# Move Back Face Itself
		self._turnFaceItself('B')
		if(self.solution is not False):
			self.solution.append('B')

	def moveCounterBack(self):
		# Move Other Faces
		tmp = copy.deepcopy(self.up)
		for n in range(0, 3):
			self.up[0][2 - n] = self.left[n][0]
			self.left[n][0] = self.down[2][n]
			self.down[2][n] = self.right[2 - n][2]
			self.right[2 - n][2] = tmp[0][2 - n]
		# Move Back Face Itself
		self._turnCounterFaceItself('B')
		if(self.solution is not False):
			self.solution.append('B\'')

	def moveBackHalf(self):
		self.moveBack()
		self.moveBack()

	def moveUp(self):
		# Move Other Faces
		tmp = copy.deepcopy(self.back)
		self.back[0] = self.left[0]
		self.left[0] = self.front[0]
		self.front[0] = self.right[0]
		self.right[0] = tmp[0]
		# Move Up Face Itself
		self._turnFaceItself('U')
		if(self.solution is not False):
			self.solution.append('U')

	def moveCounterUp(self):
		# Move Other Faces
		tmp = copy.deepcopy(self.left)
		self.left[0] = self.back[0]
		self.back[0] = self.right[0]
		self.right[0] = self.front[0]
		self.front[0] = tmp[0]
		# Move Up Face Itself
		self._turnCounterFaceItself('U')
		if(self.solution is not False):
			self.solution.append('U\'')

	def moveUpHalf(self):
		self.moveUp()
		self.moveUp()

	def moveDown(self):
		tmp = copy.deepcopy(self.left)
		# Move Other Faces
		self.left[2] = self.back[2]
		self.back[2] = self.right[2]
		self.right[2] = self.front[2]
		self.front[2] = tmp[2]
		# Move Down Face Itself
		self._turnFaceItself('D')
		if(self.solution is not False):
			self.solution.append('D')

	def moveCounterDown(self):
		tmp = copy.deepcopy(self.left)
		# Move Other Faces
		self.left[2] = self.front[2]
		self.front[2] = self.right[2]
		self.right[2] = self.back[2]
		self.back[2] = tmp[2]
		# Move Down Face Itself
		self._turnCounterFaceItself('D')
		if(self.solution is not False):
			self.solution.append('D\'')

	def moveDownHalf(self):
		self.moveDown()
		self.moveDown()

	def _turnFaceItself(self, face):
		if face not in self.structure.keys():
			raise ValueError(constants.ERROR_FACE)
		originalFace = copy.deepcopy(self.structure[face])
		# Move Corner
		self.structure[face][0][0] = originalFace[2][0]
		self.structure[face][0][2] = originalFace[0][0]
		self.structure[face][2][0] = originalFace[2][2]
		self.structure[face][2][2] = originalFace[0][2]
		# Move Side
		self.structure[face][1][0] = originalFace[2][1]
		self.structure[face][2][1] = originalFace[1][2]
		self.structure[face][1][2] = originalFace[0][1]
		self.structure[face][0][1] = originalFace[1][0]

	def _turnCounterFaceItself(self, face):
		if face not in self.structure.keys():
			raise ValueError(constants.ERROR_FACE)
		originalFace = copy.deepcopy(self.structure[face])
		# Move Corner
		self.structure[face][0][0] = originalFace[0][2]
		self.structure[face][0][2] = originalFace[2][2]
		self.structure[face][2][0] = originalFace[0][0]
		self.structure[face][2][2] = originalFace[2][0]
		# Move Side
		self.structure[face][1][0] = originalFace[0][1]
		self.structure[face][2][1] = originalFace[1][0]
		self.structure[face][1][2] = originalFace[2][1]
		self.structure[face][0][1] = originalFace[1][2]
