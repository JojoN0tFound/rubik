import constants

def parseMovement(movement):
	if((not isinstance(movement, str)) or (1 <= len(movement) <= 2) is False):
		return False
	if len(movement) == 2 and (movement[1] != "'" and movement[1] != '2'):
		return False
	if(movement[0] not in constants.movements):
		return False
	return True

def parsing(argv, argc):
	if(argc != 3 or len(argv[1]) == 0 or (argv[2] != "-h" and argv[2] != '-t')):
		return False
	sequence = argv[1].split()
	for movement in sequence:
		if(parseMovement(movement) is False):
			return False
	return True
