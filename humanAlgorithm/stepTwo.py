from utils import verifyStepTwo
from constants import color
from string import Template
import constants


def _getWhiteTopCorner(rubik, face):
	goodPositions = [True, True]
	goodPositions[0] = True if rubik.structure[face][0][0] == 'W' else False
	goodPositions[1] = True if rubik.structure[face][0][2] == 'W' else False
	return goodPositions


def _getWhiteBottomCorner(rubik, face):
	goodPositions = [True, True]
	goodPositions[0] = True if rubik.structure[face][2][0] == 'W' else False
	goodPositions[1] = True if rubik.structure[face][2][2] == 'W' else False
	return goodPositions


def _getWhiteDownCorner(rubik):
	goodPositions = [True, True, True, True]
	goodPositions[0] = True if rubik.down[0][0] == 'W' else False
	goodPositions[1] = True if rubik.down[0][2] == 'W' else False
	goodPositions[2] = True if rubik.down[2][0] == 'W' else False
	goodPositions[3] = True if rubik.down[2][2] == 'W' else False
	return goodPositions


def _alignWhiteDownCorner(rubik, pickOneDownCorner):
	faceItr = ["L", "F", "R", "B"]
	if(pickOneDownCorner == 0):
		leftColor = rubik.left[2][2]
		topColor = rubik.front[2][0]
	if(pickOneDownCorner == 1):
		leftColor = rubik.front[2][2]
		topColor = rubik.right[2][0]
	if(pickOneDownCorner == 2):
		leftColor = rubik.back[2][2]
		topColor = rubik.left[2][0]
	if(pickOneDownCorner == 3):
		leftColor = rubik.right[2][2]
		topColor = rubik.back[2][0]
	while(rubik.structure[color[leftColor]][2][0] != topColor 
			or rubik.structure[color[topColor]][2][2] != leftColor):
		rubik.moveDown()
	shuffle = Template("$right' D2 $right D $right' D' $right").substitute(
		right=faceItr[(faceItr.index(color[leftColor]) + 1) % 4])
	rubik.startShuffle(shuffle)


def _alignWhiteBottomCorner(rubik, z, pickOneCorner):
	faceItr = ['L', 'F', 'R', 'B']
	oppositeCorner = rubik.structure[faceItr[(faceItr.index(z) + 1) % 4]][2][0] if pickOneCorner == 1 else rubik.structure[faceItr[(faceItr.index(z) - 1) % 4]][2][2]
	if(pickOneCorner == 0):
		while(rubik.structure[color[oppositeCorner]][2][2] != oppositeCorner or rubik.structure[faceItr[(faceItr.index(color[oppositeCorner]) + 1) % 4]][2][0] != 'W'):
			rubik.moveDown()
		rubik.startShuffle(
			constants.stepTwoBottomCorner[color[oppositeCorner]][pickOneCorner])

	if(pickOneCorner == 1):
		while(rubik.structure[color[oppositeCorner]][2][0] != oppositeCorner or rubik.structure[faceItr[(faceItr.index(color[oppositeCorner]) - 1) % 4]][2][2] != 'W'):
			rubik.moveDown()
		rubik.startShuffle(
			constants.stepTwoBottomCorner[color[oppositeCorner]][pickOneCorner])


def _wrongUpSpot(rubik):
	faceItr = ['L', 'F', 'R', 'B']
	for z in faceItr:
		leftFace = faceItr[(faceItr.index(z) - 1) % 4]
		rightFace = faceItr[(faceItr.index(z) + 1) % 4]
		if(rubik.structure[z][0][0] != rubik.structure[z][1][1]):
			rubik.startShuffle(leftFace + " D " + leftFace + "'")
			break
		if(rubik.structure[z][0][2] != rubik.structure[z][1][1]):
			rubik.startShuffle(rightFace + "'" + " D " + rightFace)
			break


def stepTwo(rubik):
	if(verifyStepTwo(rubik) is True):
		return
	faceItr = ['L', 'F', 'R', 'B']
	while(verifyStepTwo(rubik) is False):
		for z in faceItr:
			while(True in _getWhiteBottomCorner(rubik, z)):
				pickOneBottomCorner = _getWhiteBottomCorner(
					rubik, z).index(True)
				_alignWhiteBottomCorner(rubik, z, pickOneBottomCorner)
			if(True in _getWhiteTopCorner(rubik, z)):
				pickOneTopCorner = _getWhiteTopCorner(rubik, z).index(True)
				shuffle = Template("$face D $face'").substitute(face=faceItr[(faceItr.index(
					z) - 1) % 4]) if pickOneTopCorner == 0 else Template("$face' D $face").substitute(face=faceItr[(faceItr.index(z) + 1) % 4])
				rubik.startShuffle(shuffle)
		if(True in _getWhiteDownCorner(rubik)):
			pickOneDownCorner = _getWhiteDownCorner(rubik).index(True)
			_alignWhiteDownCorner(rubik, pickOneDownCorner)
		else:
			_wrongUpSpot(rubik)
