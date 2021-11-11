from thistlethwaite.utils import getEdge, getCorner

# Orient all corners, and place FR, RB, BL, LF in the correct slice.
def G1_G2(state):
	result = getCorner(state)
	result.append(0)

	edge = getEdge(state, 1)
		
	for e in range(12):
		result[8] = result[8] | int(edge[e] / 8) << e

	return tuple(result)

# ...
def G2_G3(state):
	result = [0, 0, 0]
		
	edge = getEdge(state, 1)
	corner = getCorner(state, 1)

	for e in range(12):
		result[0] = result[0] | ( (2 if (edge[e] >= 8) else (edge[e] & 1)) << (2*e))
		
	for c in range(8):
		result[1] = result[1] | ((corner[c] & 5) << (3*c))
		
	for i in range(8):
		for j in range(i+1, 8):
			result[2] = result[2] ^ int(corner[i] > corner[j])

	return tuple(result)
