from utils import verifyStepSix
from string import Template
from random import choice


def stepSix(rubik):
	oppositeItr = ['F', 'R', 'L', 'B']
	faceItr = ['F', 'L', 'B', 'R']
	while(False in verifyStepSix(rubik)):
		cornerPositions = verifyStepSix(rubik)
		pickUpOne = cornerPositions.index(
			True) if True in cornerPositions else False
		if(pickUpOne is not False):
			front = oppositeItr[pickUpOne]
			right = faceItr[(faceItr.index(front) + 1) % 4]
			left = faceItr[(faceItr.index(front) - 1) % 4]
			rubik.startShuffle(
				Template("D $right D' $left' D $right' D' $left").substitute(
					left=left, front=front, right=right))
		else:
			front = choice(oppositeItr)
			right = faceItr[(faceItr.index(front) + 1) % 4]
			left = faceItr[(faceItr.index(front) - 1) % 4]
			rubik.startShuffle(
				Template("D $right D' $left' D $right' D' $left").substitute(
					left=left, front=front, right=right))
