from utils import verifyStepFour
from string import Template


def _getYellowEdge(rubik):
	edgePositions = [True, True, True, True]
	edgePositions[0] = True if rubik.down[0][1] == 'Y' else False
	edgePositions[1] = True if rubik.down[1][0] == 'Y' else False
	edgePositions[2] = True if rubik.down[2][1] == 'Y' else False
	edgePositions[3] = True if rubik.down[1][2] == 'Y' else False
	return edgePositions


def _isDot(rubik):
	return rubik.down[0][1] != 'Y' and rubik.down[1][0] != 'Y' and rubik.down[1][2] != 'Y' and rubik.down[2][1] != 'Y'


def _isLShape(rubik):
	edgePositions = _getYellowEdge(rubik)
	if(edgePositions.count(True) != 2):
		return False
	elif(edgePositions[0] and edgePositions[1]):
		return 'B'
	elif(edgePositions[0] and edgePositions[3]):
		return 'L'
	elif(edgePositions[1] and edgePositions[2]):
		return 'R'
	elif(edgePositions[2] and edgePositions[3]):
		return 'F'
	else:
		return False


def _isHorizontal(rubik):
	edgePositions = _getYellowEdge(rubik)
	if(edgePositions.count(True) != 2):
		return False
	elif(edgePositions[0] and edgePositions[2]):
		return 'L' if rubik.structure['L'][2][1] == 'Y' else 'R'
	elif(edgePositions[1] and edgePositions[3]):
		return 'B' if rubik.structure['B'][2][1] == 'Y' else 'F'
	else:
		return False


def stepFour(rubik):
	faceItr = ['F', 'L', 'B', 'R']
	shuffle = Template("$front $right D $right' D' $front'")
	if(verifyStepFour(rubik)):
		return
	if(_isHorizontal(rubik) is not False):
		front = _isHorizontal(rubik)
		rubik.startShuffle(shuffle.substitute(front=_isHorizontal(
			rubik), right=faceItr[(faceItr.index(front) + 1) % 4]))
	if(_isDot(rubik)):
		for z in faceItr:
			if(rubik.structure[z][2][1] == 'Y'):
				rubik.startShuffle(shuffle.substitute(
					front=z, right=faceItr[(faceItr.index(z) + 1) % 4]))
				break
	if(_isLShape(rubik) is not False):
		front = _isLShape(rubik)
		rubik.startShuffle(Template("$front D $right D' $right' $front'").substitute(
			front=front, right=faceItr[(faceItr.index(front) + 1) % 4]))
