# Advent of Code 2018 Day 6 Part 2
# Author: Aaron Leong

from part1version2 import gridDistance, get2dCoordinatesFurtherstFromOrigin, readInputs

def findDistances(listOfCoordinates):
	pointFurthestFromOrigin = get2dCoordinatesFurtherstFromOrigin(listOfCoordinates)
	numOfCol = pointFurthestFromOrigin[0] + 1
	numOfRow = pointFurthestFromOrigin[1] + 1
	result = []
	for rowNum in range(0, numOfRow):
		rowResult = []
		for colNum in range(0, numOfCol):
			print(rowNum, colNum)
			totalDistance = 0
			for coordinates in listOfCoordinates:
				totalDistance += gridDistance((colNum, rowNum), coordinates)
			rowResult.append(totalDistance)
		result.append(rowResult)
	return(result)

def countNumberOfCoordinatesWithinRange(maxDistance, twoDMapOfDistances):
	count = 0
	numOfCol = len(twoDMapOfDistances[0])
	numOfRow = len(twoDMapOfDistances)
	for rowNum in range(0, numOfRow):
		for colNum in range(0, numOfCol):
			cell = twoDMapOfDistances[rowNum][colNum]
			if cell < maxDistance:
				count += 1
	return(count)

if __name__ == "__main__":
	
	#################### Test Part 2
	
	testListOfCoordinates = [
		(1, 1),
		(1, 6),
		(8, 3),
		(3, 4),
		(5, 5),
		(8, 9)
	]
	
	testDistances = findDistances(testListOfCoordinates)
	#print(testDistances)
	testNumOfCoordinates = countNumberOfCoordinatesWithinRange(32, testDistances)
	print(testNumOfCoordinates == 16)