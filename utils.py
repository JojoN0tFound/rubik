from object.classRubik import Rubik

def verifyCompleteCross(rubik):
	if(rubik.up[0][1] != 'W'
			or rubik.up[1][0] != 'W'
			or rubik.up[1][2] != 'W'
			or rubik.up[2][1] != 'W'):
		return False
	if(rubik.left[0][1] != 'O' or rubik.right[0][1] != 'R'
	   or rubik.front[0][1] != 'G' or rubik.back[0][1] != 'B'):
		return False
	return True


def verifyStepTwo(rubik):
	if(verifyCompleteCross(rubik) is False
			or rubik.up[0][0] != 'W' or rubik.up[0][2] != 'W'
			or rubik.up[2][0] != 'W' or rubik.up[2][2] != 'W'):
		return False
	faceItr = ["L", "R", "B", "F"]
	for z in faceItr:
		if(rubik.structure[z][0][0] != rubik.structure[z][1][1]
				or rubik.structure[z][0][2] != rubik.structure[z][1][1]):
			return False
	return True


def verifyStepThree(rubik):
	if(verifyCompleteCross(rubik) is False or verifyStepTwo(rubik) is False):
		return False
	faceItr = ["L", "F", "R", "B"]
	for z in faceItr:
		if(rubik.structure[z][1][0] != rubik.structure[z][1][1]
				or rubik.structure[z][1][2] != rubik.structure[z][1][1]):
			return False
	return True


def verifyStepFour(rubik):
	if(verifyCompleteCross(rubik) is False
			or verifyStepTwo(rubik) is False
			or verifyStepThree(rubik) is False):
		return False
	if(rubik.down[0][1] != 'Y' or rubik.down[1][0] != 'Y'
			or rubik.down[1][2] != 'Y' or rubik.down[2][1] != 'Y'):
		return False
	return True


def verifyStepFive(rubik):
	faceItr = ['F', 'L', 'B', 'R']
	if(verifyCompleteCross(rubik) is False or verifyStepTwo(rubik) is False
			or verifyStepThree(rubik) is False or verifyStepFour(rubik) is False):
		return False
	for z in faceItr:
		if(rubik.structure[z][2][1] != rubik.structure[z][1][1]):
			return False
	return True


def verifyStepSix(rubik):
	if(verifyCompleteCross(rubik) is False or verifyStepTwo(rubik) is False
			or verifyStepThree(rubik) is False or verifyStepFour(rubik) is False
			or verifyStepFive(rubik) is False):
		return False
	goodCorner = [False, False, False, False]
	first = [rubik.down[0][0], rubik.front[2][0], rubik.left[2][2]]
	second = [rubik.down[0][2], rubik.front[2][2], rubik.right[2][0]]
	third = [rubik.down[2][0], rubik.left[2][0], rubik.back[2][2]]
	fourth = [rubik.down[2][2], rubik.right[2][2], rubik.back[2][0]]
	if('Y' in first and 'G' in first and 'O' in first):
		goodCorner[0] = True
	if('Y' in second and 'G' in second and 'R' in second):
		goodCorner[1] = True
	if('Y' in third and 'O' in third and 'B' in third):
		goodCorner[2] = True
	if('Y' in fourth and 'R' in fourth and 'B' in fourth):
		goodCorner[3] = True
	return goodCorner


def verifyRubik(rubik):
	if(rubik.left != [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
			or rubik.right != [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
			or rubik.up != [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
			or rubik.down != [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]
			or rubik.front != [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
			or rubik.back != [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]):
		return False
	return True

def verifySolution(shuffle,solution):
	rubik = Rubik(shuffle)
	rubik.startShuffle(solution)
	return verifyRubik(rubik)