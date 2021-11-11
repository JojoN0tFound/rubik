from object.classRubik import Rubik
from humanAlgorithm.stepOne import stepOne
from humanAlgorithm.stepTwo import stepTwo
from humanAlgorithm.stepThree import stepThree
from humanAlgorithm.stepFour import stepFour
from humanAlgorithm.stepFive import stepFive
from humanAlgorithm.stepSix import stepSix
from humanAlgorithm.stepSeven import stepSeven
from utils import verifyRubik
import constants
import sys

def humanResolve(shuffle):
	rubik = Rubik(shuffle)
	rubik.solution = []
	stepOne(rubik)
	stepTwo(rubik)
	stepThree(rubik)
	stepFour(rubik)
	stepFive(rubik)
	stepSix(rubik)
	stepSeven(rubik)
	if(verifyRubik(rubik) is False):
		sys.exit(constants.ERROR_RESOLVE)
	return rubik.solution
