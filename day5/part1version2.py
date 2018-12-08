# Advent of Code 2018 Day 5 Part 1 Version 2
# Author: Aaron Leong

def processString(string):
	listOfLetters = list(string)
	currentLength = len(string)
	start = 0
	possible = True
	while possible:
		print("Current length: " + str(currentLength))
		print(listOfLetters[-5:])
		for i in range(start, len(listOfLetters) - 1, 1):
			curr = listOfLetters[i]
			next = listOfLetters[i+1]
			#print(i)
			#print(len(listOfLetters) - 1)
			if (curr.lower() == next.lower()) and ((curr.isupper() and next.islower()) or (curr.islower() and next.isupper())):
				listOfLetters = listOfLetters[:i] + listOfLetters[i+2:]
				currentLength = len(listOfLetters)
				start = i - 1 if i - 1 > 0 else 0
				break
			if i == len(listOfLetters) - 2:
				#print(i)
				#print(len(listOfLetters) - 2)
				possible = False
	
	finalString = "".join(listOfLetters)
	return(len(finalString), finalString)
		


if __name__ == "__main__":
	
	######### part 1 test
	print("########## Part 1 Test ##########")
	
	testString = "dabAcCaCBAcCcaDA"
	expectedOutput = "dabCBAcaDA"
	print("Test #1:")
	
	print(processString(testString))
	print(processString(testString) == (len(expectedOutput), expectedOutput))
	
	######### part 1 actual
	print("########## Part 1 Actual ##########")
	f = open("input.txt", "r")
	inputString = f.read()
	print(processString(inputString))