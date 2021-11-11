# General Constants
movements = ['F', 'R', 'U', 'B', 'L', 'D']
allMovements = ['F', 'R', 'U', 'B', 'L', 'D',
				'F\'', 'R\'', 'U\'', 'B\'', 'L\'', 'D\'',
				'F2', 'R2', 'U2', 'B2', 'L2', 'D2']
color = {
	"G": "F",
	"R": "R",
	"O": "L",
	"B": "B",
	"W": "U",
	"Y": "D"
}

# SuperFlip Mix for testing
hardestMix1 = "U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2"
hardestMix2 = "F U' F2 D' B U R' F' L D' R' U' L U B' D2 R' F U2 D2"

# Error Message
ERROR_PARSING = "Usage: python3 main.py \"L R2 B' F U' D2\" -[ht]\n-h : human algorithm (fast but lots of movement)\n-t : thistlethwaite algorithm (less movements but slower)"
ERROR_FACE = "turnFaceItselfError: This Face doesn't exist."
ERROR_MOVEMENT = "parseMovement: bad Movement"
ERROR_RESOLVE = "Algorithm : Not Resolved"

# StepOne Algorithm : Bring the edge to the down face according to face
# and edge position
stepOne = {
	"F": ["F' L D L'", "L D L'", "R' D' R", "D R F R'"],
	"R": ["R' F D F'", "F D F'", "B' D' B", "D B R B'"],
	"B": ["B' R D R'", "R D R'", "L' D' L", "D L B L'"],
	"L": ["L' B D B'", "B D B'", "F' D' F", "D F L F'"]
}

# StepTwo Algorithm - Complete the White Face :

stepTwoBottomCorner = {
	"F": ["R' D' R", "L D L'"],
	"R": ["B' D' B", "F D F'"],
	"B": ["L' D' L", "R D R'"],
	"L": ["F' D' F", "B D B'"]
}
