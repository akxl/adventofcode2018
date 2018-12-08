# Advent of Code 2018 Day 5 Part 1
# Author: Aaron Leong

def processString(string):
	listOfLetters = list(string)
	currentLength = len(string)
	possible = True
	while possible:
		print("Current length: " + str(currentLength))
		print(listOfLetters[-5:])
		for i in range(0, len(listOfLetters) - 1):
			curr = listOfLetters[i]
			next = listOfLetters[i+1]
			#print(i)
			#print(len(listOfLetters) - 1)
			if (curr.lower() == next.lower()) and ((curr.isupper() and next.islower()) or (curr.islower() and next.isupper())):
				listOfLetters = listOfLetters[:i] + listOfLetters[i+2:]
				currentLength = len(listOfLetters)
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
	
	print("########## Part 1 Actual ##########")
	f = open("input.txt", "r")
	inputString = f.read()
	print(processString(inputString))