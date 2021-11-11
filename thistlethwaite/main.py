from thistlethwaite.classCubeState import cubeState
from thistlethwaite.constants import phase_moves
from thistlethwaite.utils import moveToStr

"""
	1 - DataStructure :
			6 32-bit integers:
				0x11111111 X 6 Faces
			Bytes Face Representation :
			
			0 1 2
			7   3
			6 5 4

			Each number represent a color (half byte).
			
			One Face is represented by 4 bytes.
			
			Twisting can be done using bitwise operations,
			and face comparisons can be done using masks and 32-bit integer comparison.
		
	2 - Thistlethwaite :

"""
def thistlethwaite(shuffle):
	goalState = cubeState([
		0x00000000, # == 0000 X 8 => W
		0x11111111, # == 0001 X 8 => Y
		0x22222222,  # == 0011 X 8 => G
		0x33333333, # == 0011 X 8 => B
		0x44444444, # == 0100 X 8 => O
		0x55555555, # == 0101 X 8 => R
	])

	state = cubeState(goalState.state)
	state.shuffle(shuffle)

	for phase in range(4):
		state_id = state.phase(phase)
		goal_id = goalState.phase(phase)
		states = [state]
		state_ids = set([state_id])
		if state_id != goal_id:
			phase_ok = False
			while not phase_ok:
				next_states = []
				for cur_state in states:
					for move in phase_moves[phase]:
						next_state = cur_state.move(move)
						next_id = next_state.phase(phase)
						if next_id == goal_id:
							solution = ' '.join([moveToStr(m) for m in next_state.path]) 
							phase_ok = True
							state = next_state
							break
						if next_id not in state_ids:
							state_ids.add(next_id)
							next_states.append(next_state)
					if phase_ok:
						break
				states = next_states
	return solution
