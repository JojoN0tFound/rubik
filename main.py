from utils import verifySolution
from parsing import parsing
from humanAlgorithm.main import humanResolve
from thistlethwaite.main import thistlethwaite
from optimization import optimization
import sys
import constants

def main():
	if(parsing(sys.argv, len(sys.argv)) is False):
		return sys.exit(constants.ERROR_PARSING)
	solution = optimization(humanResolve(sys.argv[1])) if sys.argv[2] == '-h' else thistlethwaite(sys.argv[1])
	print(solution)
	# Remove the following comment to print boolean represents whether the rubik is fully solved or not
	# print(verifySolution(sys.argv[1], solution))

if __name__ == "__main__":
	main()