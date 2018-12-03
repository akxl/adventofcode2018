# which position occurs 2 times first?

# this is quite slow
def getPositionWithTwoOccurences(numbers):
	history = [0]
	currentPosition = 0
	found = False
	while (found == False):
		for number in numbers:
			currentPosition += number
			if currentPosition in history:
				print("The first position with 2 occurences is: %d" % (currentPosition))
				found = True
				return(currentPosition)
			else:
				history.append(currentPosition)


if __name__ == "__main__":
	
	f = open("input.txt", "r")
	numbers = list(map(int, f.read().split()))
	print(sum(numbers)) # expect 576
	
	print(getPositionWithTwoOccurences([1, -1])) # expect 0
	print(getPositionWithTwoOccurences([3,3,4,-2,-4])) # expect 10
	print(getPositionWithTwoOccurences([-6,3,8,5,-6])) # expect 5
	print(getPositionWithTwoOccurences([7,7,-2,-7,-4])) # expect 14
	print(getPositionWithTwoOccurences(numbers)) # 77674
	
	
	