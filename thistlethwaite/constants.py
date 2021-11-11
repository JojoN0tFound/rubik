# Face, Color => Number
U, UP, WHITE = 0, 0, 0
D, DOWN, YELLOW = 1, 1, 1
F, FRONT, GREEN = 2, 2, 2
B, BACK, BLUE = 3, 3, 3
L, LEFT, ORANGE = 4, 4, 4
R, RIGHT, RED = 5, 5, 5

strToMove = {
		"U": 0,
		"U2": 1,
		"U'": 2,
		"D": 3,
		"D2": 4,
		"D'": 5,
		"F": 6,
		"F2": 7,
		"F'": 8,
		"B": 9,
		"B2": 10,
		"B'": 11,
		"L": 12,
		"L2": 13,
		"L'": 14,
		"R": 15,
		"R2": 16,
		"R'": 17
}

"""
G0=<L, R, F, B, U, D>		
G1=<L, R, F2, B2, U,D>		
G2=<L2, R2, F2,B2,U,D>		
G3=<L2,R2,F2,B2,U2,D2>
G4=I	1

Authorized moves per phases
"""
phase_moves = [
				[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
				[0, 1, 2, 3, 4, 5, 7, 10, 12, 13, 14, 15, 16, 17],
				[0, 1, 2, 3, 4, 5, 7, 10, 13, 16],
				[1, 4, 7, 10, 13, 16]
			]


edge = {
	(UP, FRONT): 0,
	(FRONT, UP): 0,
	(UP, RIGHT): 1,
	(RIGHT, UP): 1,
	(UP, BACK): 2,
	(BACK, UP): 2,
	(UP, LEFT): 3,
	(LEFT, UP): 3,
	(DOWN, FRONT): 4,
	(FRONT, DOWN): 4,
	(DOWN, RIGHT): 5,
	(RIGHT, DOWN): 5,
	(DOWN, BACK): 6,
	(BACK, DOWN): 6,
	(DOWN, LEFT): 7,
	(LEFT, DOWN): 7,
	(FRONT, RIGHT): 8,
	(RIGHT, FRONT): 8,
	(FRONT, LEFT): 9,
	(LEFT, FRONT): 9,
	(BACK, RIGHT): 10,
	(RIGHT, BACK): 10,
	(BACK, LEFT): 11,
	(LEFT, BACK): 11  
}

corner = {
	frozenset([U, F, R]): 0,
	frozenset([U, B, R]): 1,
	frozenset([U, B, L]): 2,
	frozenset([U, F, L]): 3,
	frozenset([D, F, R]): 4,
	frozenset([D, F, L]): 5,
	frozenset([D, L, B]): 6,
	frozenset([D, B, R]): 7,
}

# Constants to move cubeStates
adjacentMask = {
	0: 0x00000FFF,
	1: 0x0FFF0000,
	2: 0x0FFF0000,
	3: 0x00000FFF,
	4: 0xFF00000F,
	5: 0x000FFF00,
}
