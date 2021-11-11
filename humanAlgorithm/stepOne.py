import utils
import constants
from object.classRubik import Rubik


def _getWhiteEdges(rubik, face):
	goodPositions = [True, True, True, True]
	goodPositions[0] = True if rubik.structure[face][0][1] == 'W' else False
	goodPositions[1] = True if rubik.structure[face][1][0] == 'W' else False
	goodPositions[2] = True if rubik.structure[face][1][2] == 'W' else False
	goodPositions[3] = True if rubik.structure[face][2][1] == 'W' else False
	return goodPositions

# This function verify if i have at least one fully complete white edge on
# the upper face and return the opposite face. else return false


def _isOneGoodUpperEdge(rubik):
	if(rubik.up[0][1] == 'W' and rubik.back[0][1] == 'B'):
		return 'B'
	elif(rubik.up[1][0] == 'W' and rubik.left[0][1] == 'O'):
		return 'L'
	elif(rubik.up[1][2] == 'W' and rubik.right[0][1] == 'R'):
		return 'R'
	elif(rubik.up[2][1] == 'W' and rubik.front[0][1] == 'G'):
		return 'F'
	return False

# This function return the first opposite edge of a bad white edge on the
# upper face.


def _takeOneBadUpperEdge(rubik):
	if(rubik.up[0][1] == 'W' and rubik.back[0][1] != 'B'):
		return 'B'
	elif(rubik.up[1][0] == 'W' and rubik.left[0][1] != 'O'):
		return 'L'
	elif(rubik.up[1][2] == 'W' and rubik.right[0][1] != 'R'):
		return 'R'
	elif(rubik.up[2][1] == 'W' and rubik.front[0][1] != 'G'):
		return 'F'
	return False


def _isOneGoodDownEdge(rubik):
	if(rubik.down[0][1] == 'W' and rubik.front[2][1] == 'G'):
		return "F2"
	elif(rubik.down[1][0] == 'W' and rubik.left[2][1] == 'O'):
		return "L2"
	elif(rubik.down[1][2] == 'W' and rubik.right[2][1] == 'R'):
		return "R2"
	elif(rubik.down[2][1] == 'W' and rubik.back[2][1] == 'B'):
		return "B2"
	return False


def _getDownEdgeToUp(rubik):
	whiteEdgeInDown = _getWhiteEdges(rubik, "D")
	if((True in whiteEdgeInDown) is False):
		return
	isOneGoodEdge = _isOneGoodDownEdge(rubik)
	while(isOneGoodEdge is False):
		rubik.moveDown()
		isOneGoodEdge = _isOneGoodDownEdge(rubik)

	rubik.startShuffle(isOneGoodEdge)


def _verifyMoveBottomEdge(rubik, z):
	if((z == 'F' and rubik.up[2][1] == 'W')
			or (z == 'B' and rubik.up[0][1] == 'W')
			or (z == 'L' and rubik.up[1][0] == 'W')
			or (z == 'R' and rubik.up[1][2] == 'W')):
		return True
	else:
		return False


def _moveBottomEdge(rubik, z):
	faceItr = ['F', 'B', 'L', 'R']
	for z in faceItr:
		if(_verifyMoveBottomEdge(rubik, z) is True):
			# rubik.startShuffle("D L F B R")
			rubik.startShuffle("D L R")


def _specialCase(rubik):
	# Special Case : When we already have the white cross without good colors
	# First , we verify if we need just simple U rotation to match the perfect
	# cross.
	for i in range(0, 4):
		rubik.moveUp()
		if(utils.verifyCompleteCross(rubik) is True):
			return
	# We apply the specific case here
	rubik.startShuffle(_takeOneBadUpperEdge(rubik) + '2')


def stepOne(rubik):
	# Verify if we already completed the Step One.
	if(utils.verifyCompleteCross(rubik)):
		return
	whiteEdgeInUpper = _getWhiteEdges(rubik, "U")
	# If we have one or more white edge in upper Face then place just one
	# correctly (with good colors).
	if(True in whiteEdgeInUpper):
		while(_isOneGoodUpperEdge(rubik) is False):
			rubik.moveUp()
	# Place Other white edges with right colors
	faceItr = ["F", "R", "B", "L"]
	while(True in _getWhiteEdges(rubik, "F")
			or True in _getWhiteEdges(rubik, "R")
			or True in _getWhiteEdges(rubik, "B")
			or True in _getWhiteEdges(rubik, "L")):
		for z in faceItr:
			while(True in _getWhiteEdges(rubik, z)):
				pickOneEdge = _getWhiteEdges(rubik, z).index(True)
				# Special case
				if(pickOneEdge == 3
						and _verifyMoveBottomEdge(rubik, z) is True):
					_moveBottomEdge(rubik, z)
				else:
					rubik.startShuffle(
						constants.stepOne[z][pickOneEdge])
					_getDownEdgeToUp(rubik)

	# Take white edge on down to the upper face.
	while(utils.verifyCompleteCross(rubik) is False):
		if(all(_getWhiteEdges(rubik, "U")) is True):
			_specialCase(rubik)
		else:
			_getDownEdgeToUp(rubik)
