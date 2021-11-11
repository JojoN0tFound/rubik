from utils import verifyRubik


def _wrongCornerToFRU(rubik):
	first = [rubik.down[0][0], rubik.front[2][0], rubik.left[2][2]]
	while((rubik.down[0][0] == 'Y' and rubik.front[2][0] == 'G' and rubik.left[2][2] == 'O') or rubik.down[0][0] == 'Y'):
		rubik.moveDown()


def _tryMoveDown(rubik):
	if(verifyRubik(rubik)):
		return True
	for i in range(3):
		rubik.moveDown()
		if(verifyRubik(rubik)):
			return True
	return False


def stepSeven(rubik):
	if(_tryMoveDown(rubik)):
		return
	while(rubik.down[0][0] != 'Y' or rubik.down[0][2] != 'Y' or rubik.down[2][0] != 'Y' or rubik.down[2][2] != 'Y'):
		_wrongCornerToFRU(rubik)
		while(rubik.down[0][0] != 'Y'):
			rubik.startShuffle("L' U' L U")
	_tryMoveDown(rubik)
