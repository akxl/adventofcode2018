# Advent of Code 2018 Part 2
# Author: Aaron Leong

import sys
from part1version2 import processString 

def getUniqueComponents(string):
	result = set()
	for letter in list(string):
		result.add(letter.lower())
	return(result)

def removeComponent(string, component):
	start = 0
	listOfLetters = list(string)
	possible = True
	while possible:
		for i in range(start, len(listOfLetters), 1):
			if listOfLetters[i] == component.lower() or listOfLetters[i] == component.upper():
				listOfLetters = listOfLetters[:i] + listOfLetters[i+1:]
				start = i-1 if i-1 > 0 else 0
				break
			if i == len(listOfLetters) - 1:
				possible = False
	return("".join(listOfLetters))

def findShortest(string):
	minLength = sys.maxsize
	minLengthString = "none"
	for component in list(getUniqueComponents(string)):
		print("Current component: " + str(component))
		shortenedString = removeComponent(string, component)
		processedString = processString(shortenedString)
		if processedString[0] < minLength:
			minLength = processedString[0]
			minLengthString = processedString[1]
	return(minLength, minLengthString)

if __name__ == "__main__":
	
	######### part 2 test
	print("########## Part 2 Tests ##########")
	testString = "dabAcCaCBAcCcaDA"
	print(getUniqueComponents(testString) == {"a", "d", "b", "c"})
	testReducedString1 = removeComponent(testString, "a")
	print(testReducedString1 == "dbcCCBcCcD")
	testReducedString2 = removeComponent(testString, "b")
	print(testReducedString2 == "daAcCaCAcCcaDA")
	testReducedString3 = removeComponent(testString, "c")
	print(testReducedString3 == "dabAaBAaDA")
	testReducedString4 = removeComponent(testString, "d")
	print(testReducedString4 == "abAcCaCBAcCcaA")
	print(processString(testReducedString1) == (6, "dbCBcD"))
	print(processString(testReducedString2) == (8, "daCAcaDA"))
	print(processString(testReducedString3) == (4, "daDA"))
	print(processString(testReducedString4) == (6, "abCBAc"))
	print(findShortest(testString) == ((4, "daDA")))
	
	######### part 2 actual
	print("########## Part 2 Actual ##########")
	print("########## Part 1 Actual ##########")
	f = open("input.txt", "r")
	inputString = f.read()
	print(findShortest(inputString)[0])