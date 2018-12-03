if __name__ == "__main__":
	# Part 1: from an initial position of 0, using input.txt for inputs, what is the final position?
	f = open("input.txt", "r")
	numbers = (list(map(int ,f.read().split())))
	print(sum(numbers))