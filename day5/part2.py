# Advent of Code 2018 Part 2
# Author: Aaron Leong

from part1version2 import processString 

def getUniqueComponents(string):
	result = set()
	for letter in list(string):
		result.add(letter.lower())
	return(result)

def removeComponent(string, component):
	start = 0
	listOfLetters = list(string)
	for i in range(start, len(listOfLetters), 1):
		if listOfLetters[i] == component.lower() or listOfLetters[i] == component.upper():
			listOfLetters = listOfLetters[:i] + listOfLetters[i+1:]
			start = i-1 if i-1 > 0 else 0
			break
	return("".join(listOfLetters))


if __name__ == "__main__":
	
	######### part 2 test
	print("########## Part 2 Test ##########")
	testString = "dabAcCaCBAcCcaDA"
	print(getUniqueComponents(testString))
	print(removeComponent(testString, "a"))