# Advent of Code 2018 Day 5 Part 1 version 2
# Author: Aaron Leong

# In version 1, I was thinking in a very generalised way. In this version, I am going to attemp to solve this exercise by making the following assumption:
# Assuming a quadrilateral boundary bounded by the origin and the point furtherst from the origin, anything that touches these walls would be considered as having an infinite number of points that are closest to it.
# Example:

# aaaaa.cccc
# aAaaa.cccc
# aaaddecccc
# aadddeccCc
# ..dDdeeccc
# bb.deEeecc
# bBb.eeee..
# bbb.eeefff
# bbb.eeffff
# bbb.ffffFf

# for any specified point (uppercase letter), each other point that is closest to it would be displayed as lowercase version of this letter. The fullstop is used to denote a point with one or more closest specified points. So every lowercase letter at the edges means that its uppercased point has an infinite number of closest points (in the above example, these are A, B, C and D). Assume that fullstops don't count.

import sys

def gridDistance(vector1, vector2):
	if (len(vector1) != len(vector2)):
		raise ValueError("vector1 and vector2 must have the same dimension/length")
	length = len(vector1)
	distance = 0
	for i in range(0, length):
		distance += abs(vector1[i] - vector2[i])
	return(distance)
	
def get2dCoordinatesFurtherstFromOrigin(listOfCoordinates):
	maxDistance = -(sys.maxsize)
	furtherstPoint = (None, None)
	for coordinates in listOfCoordinates:
		distance = gridDistance((0, 0), coordinates)
		if distance > maxDistance:
			maxDistance = distance
			furtherstPoint = coordinates
	return(furtherstPoint)

# TODO: will need to revisit logic here
def draw2dMapOfSpecifiedPoints(listOfCoordinates):
	pointFurthestFromOrigin = get2dCoordinatesFurtherstFromOrigin(listOfCoordinates)
	for i in range(0, pointFurthestFromOrigin[0] + 2):
		row = ""
		for j in range(0, pointFurthestFromOrigin[1] + 1):
			if (j, i) in listOfCoordinates:
				row += "P"
			else:
				row += "."
		print(row)
		
def drawMapOfClosestAreas(listOfCoordinates):
	pointFurthestFromOrigin = get2dCoordinatesFurtherstFromOrigin(listOfCoordinates)
	numOfCol = pointFurthestFromOrigin[0] + 1
	numOfRow = pointFurthestFromOrigin[1] + 1
	result = []
	for rowNum in range(0, numOfRow):
		rowResult = []
		for colNum in range(0, numOfCol):
			print(rowNum, colNum)
			closestLabel = -1
			closestDistance = sys.maxsize
			for label, coordinates in enumerate(listOfCoordinates):
				#print(label, coordinates, (colNum,rowNum))
				distance = gridDistance((colNum, rowNum), coordinates)
				#print(distance)
				if distance < closestDistance:
					closestLabel = label
					closestDistance = distance
				elif distance == closestDistance and label != closestLabel:
					closestLabel = "."
			rowResult.append(closestLabel)
		result.append(rowResult)
	return(result)

	
def findLabelsOnTheBoundary(twoDArray):
	labels = set()
	numOfRow = len(twoDArray)
	numOfCol = len(twoDArray[0])
	
	firstRow = twoDArray[0]
	for cell in firstRow:
		labels.add(cell)
	lastRow = twoDArray[1]
	for cell in lastRow:
		labels.add(cell)
	for rowNum in range(1, numOfRow):
		leftCell = twoDArray[rowNum][0]
		labels.add(leftCell)
		rightCell = twoDArray[rowNum][numOfCol - 1]
		labels.add(rightCell)
	return(labels)


def countArea(twoDArray, setOfInfinites):
	relevantColumns = list(range(1, len(twoDArray[0]) - 1))
	searchArea = twoDArray[1:-1]
	numOfRow = len(searchArea)
	count = {}
	for rowNum in range(0, numOfRow):
		for colNum in relevantColumns:
			label = searchArea[rowNum][colNum]
			if label not in setOfInfinites:
				if label not in list(count.keys()):
					count[label] = 1
				else:
					count[label] += 1
	return(count)
	
def findMax(dictionary):
	maxLabel = (None, -1)
	for key in dictionary.keys():
		if dictionary[key] > maxLabel[1]:
			maxLabel = (key, dictionary[key])
	return(maxLabel)
			
def readInputs(filename):
	f = open(filename, "r")
	lines = f.read().split("\n")
	result = []
	for line in lines:
		numbers = list(map(int, line.split(",")))
		result.append((numbers[0], numbers[1]))
	return(result)


if __name__ == "__main__":
	
	#################### Test Part 1
	
	testListOfCoordinates = [
		(1, 1),
		(1, 6),
		(8, 3),
		(3, 4),
		(5, 5),
		(8, 9)
	]
	
	testMapOfClosests = drawMapOfClosestAreas(testListOfCoordinates)
	testInfinites = findLabelsOnTheBoundary(testMapOfClosests)
	print(testInfinites ==  set([0,1,2,'.',5]))
	testCount = countArea(testMapOfClosests, testInfinites)
	print(testCount == {3:9, 4:17})
	print(findMax(testCount) == (4,17))
	
	#################### Actual Part 1
	input = readInputs("input.txt")
	mapOfClosest = drawMapOfClosestAreas(input)
	infinities = findLabelsOnTheBoundary(mapOfClosest)
	count = countArea(mapOfClosest, infinities)
	print(findMax(count))
	
	