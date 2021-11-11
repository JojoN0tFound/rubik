import constants
from copy import deepcopy

def _removeCounterMovement(tmp):
	newLst = []
	for mov in tmp:
		if(len(mov) == 2):
			newLst.append(mov[0])
			newLst.append(mov[0])
			newLst.append(mov[0])
		else:
			newLst.append(mov)
	return newLst

def _removeFourMovement(tmp):
	newLst = []
	i = 0
	restart = False
	while i < len(tmp):
		if(i + 4 <= len(tmp) and tmp[i] == tmp[i + 1] == tmp[i + 2] == tmp [i + 3]):
			i += 4
			restart = True
		else:
			newLst.append(tmp[i])
			i += 1
	return _removeFourMovement(newLst) if restart else newLst

def _removeThreeMovement(tmp):
	newLst = []
	i = 0
	restart = False
	while i < len(tmp):
		if(i + 3 <= len(tmp) and tmp[i] == tmp[i + 1] == tmp[i + 2]):
			newLst.append(tmp[i] + "'")
			i += 3
			restart = True
		else:
			newLst.append(tmp[i])
			i += 1
	return _removeThreeMovement(newLst) if restart else newLst

def _removeTwoMovement(tmp):
	newLst = []
	i = 0
	restart = False
	while i < len(tmp):
		if(i + 2 <= len(tmp) and tmp[i] == tmp[i + 1]):
			newLst.append(tmp[i] + "2")
			i += 2
			restart = True
		else:
			newLst.append(tmp[i])
			i += 1
	return _removeTwoMovement(newLst) if restart else newLst

def optimization(solution):
	tmp = deepcopy(solution)
	tmp = _removeCounterMovement(tmp)
	tmp = _removeFourMovement(tmp)
	tmp = _removeThreeMovement(tmp)
	tmp = _removeTwoMovement(tmp)
	return " ".join(tmp)