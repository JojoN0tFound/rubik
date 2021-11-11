from utils import verifyStepThree
from string import Template
from constants import color


def _edgeInDown(rubik):
	downEdges = [
		rubik.down[0][1],
		rubik.down[1][0],
		rubik.down[2][1],
		rubik.down[1][2]]
	faceItr = ["F", "L", "B", "R"]
	i = 0
	while(i < 4):
		if(downEdges[i] != 'Y' and rubik.structure[faceItr[i]][2][1] != 'Y'):
			return i
		i += 1
	return False


def _alignDownEdge(rubik, pos):
	faceItr = ["F", "L", "B", "R"]
	downEdges = [
		rubik.down[0][1],
		rubik.down[1][0],
		rubik.down[2][1],
		rubik.down[1][2]]
	edgeColor = downEdges[pos]
	startFrom = faceItr[pos]
	goTo = color[rubik.structure[startFrom][2][1]]
	distance = (faceItr.index(startFrom) - faceItr.index(goTo)) % 4
	for i in range(distance):
		rubik.moveDown()
	if(faceItr[(faceItr.index(goTo) + 1) % 4] == color[edgeColor]):
		# Right
		shuffle = Template("D $right D' $right' D' $front' D $front").substitute(
			front=goTo, right=faceItr[(faceItr.index(goTo) + 1) % 4])
		rubik.startShuffle(shuffle)
	else:
		# Left
		shuffle = Template("D' $left' D $left D $front D' $front'").substitute(
			front=goTo, left=faceItr[(faceItr.index(goTo) - 1) % 4])
		rubik.startShuffle(shuffle)


def _alignBadEdge(rubik):
	faceItr = ["F", "L", "B", "R"]
	for z in faceItr:
		oppositeFace = faceItr[(faceItr.index(z) + 1) % 4]
		oppositeColor = rubik.structure[oppositeFace][1][2]
		if(rubik.structure[z][1][0] != rubik.structure[z][1][1] or oppositeColor != rubik.structure[oppositeFace][1][1]):
			shuffle = Template("D $right D' $right' D' $front' D $front").substitute(
				front=z, right=faceItr[(faceItr.index(z) + 1) % 4])
			rubik.startShuffle(shuffle)
			break


def stepThree(rubik):
	while(verifyStepThree(rubik) is False):
		while(_edgeInDown(rubik) is not False):
			pos = _edgeInDown(rubik)
			_alignDownEdge(rubik, pos)
		if(verifyStepThree(rubik)):
			break
		else:
			_alignBadEdge(rubik)
