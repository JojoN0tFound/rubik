from utils import verifyStepFive
from string import Template


def _tryMoveDown(rubik):
	if(verifyStepFive(rubik)):
		return True
	for i in range(3):
		rubik.moveDown()
		if(verifyStepFive(rubik)):
			return True
	return False


def _switchOpposite(rubik):
	faceItr = ['F', 'L', 'B', 'R']
	for z in faceItr:
		if(rubik.structure[z][2][1] == rubik.structure[faceItr[(faceItr.index(z) - 2) % 4]][1][1] and
				rubik.structure[faceItr[(faceItr.index(z) - 2) % 4]][2][1] == rubik.structure[z][1][1]):
			return z
	return False


def _switchFrontLeft(rubik):
	faceItr = ['F', 'L', 'B', 'R']
	for z in faceItr:
		for i in range(4):
			if(rubik.structure[z][2][1] == rubik.structure[faceItr[(faceItr.index(z) - 1) % 4]][1][1] and
					rubik.structure[faceItr[(faceItr.index(z) - 1) % 4]][2][1] == rubik.structure[z][1][1]):
				return z
			rubik.moveDown()
	return False


def stepFive(rubik):
	if(_tryMoveDown(rubik)):
		return
	faceItr = ['F', 'L', 'B', 'R']
	while(verifyStepFive(rubik) is False):
		front = _switchFrontLeft(rubik)
		if(front is not False):
			shuffle = Template("$right D $right' D $right D2 $right' D").substitute(
				right=faceItr[(faceItr.index(front) + 1) % 4])
			rubik.startShuffle(shuffle)
		switchOpposite = _switchOpposite(rubik)
		if(switchOpposite is not False):
			shuffle = Template("$right D $right' D $right D2 $right' D").substitute(
				right=faceItr[(faceItr.index(front) + 1) % 4])
