# Advent of Code 2018 Day 5
# Author: Aaron Leong

def processString(string):
	listOfLetters = list(string)
	currentLength = len(string)
	possible = True
	while currentLength > 10:
		print("Current length: " + str(currentLength))
		print(listOfLetters[-5:])
		for i in range(0, len(listOfLetters) - 1):
			curr = listOfLetters[i]
			next = listOfLetters[i+1]
			if (curr.lower() == next.lower()) and ((curr.isupper() and next.islower()) or (curr.islower() and next.isupper())):
				listOfLetters = listOfLetters[:i] + listOfLetters[i+2:]
				currentLength = len(listOfLetters)
				break
	return(len("".join(listOfLetters)))
		


if __name__ == "__main__":
	
	######### part 1 test
	print("########## Part 1 Test ##########")
	
	testString = "dabAcCaCBAcCcaDA"
	expectedOutput = "dabCBAcaDA"
	print("Test #1:")
	
	print(processString(testString))
	print(processString(testString) == expectedOutput)
	
	print("########## Part 1 Actual ##########")
	f = open("input.txt", "r")
	inputString = f.read()
	print(processString(inputString))