# Advent of Code 2018 Day 5 Part 1
# Author: Aaron Leong

# Aim: I need to find the specified point with the largest number of other points that are closest to it, so long as that number is not infinite.
# My hypothesis is that, for a given Manhatten Grid and specified points, points that lie on the bonundary will have an infinite number of other points in the Grid that are closest to it. My question is then, how to I determine this boundary? So that I can pin point the specified points on the boundary so that I can discount them?
# My guess is that for the general case, I should search for the combinatio of specified points that I can put on the boundary that will give me the largest area.
# Or if I am lazy, I can just precalculate the boundary by hand for this particular exercise, and discount the points on said boundary.
# Note that for this exercise, the 'wall' on x=0 and y=0 are boundaries too, but the specified points on this boundary may or may not result in an infinite number of other points that are closest to said specified points.

# maybe the way to find the boundary is to maximize area but minimize perimeter?
# how do you find the minimum area that contains all points?

# maybe i can try adding one point at a time to a list (or find all possible combinations in a list of lists), and calculating the area of each permutation of that list, and find max? Question is, what happens when you use the polygon area function below when things intersect?

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
		
def areaOfPolygonIn2dEuclideanSpace(listOfCoordinates):
	numberOfCoordinates = len(listOfCoordinates)
	area = 0
	j = numberOfCoordinates - 1
	for i in range(numberOfCoordinates):
		area += ((listOfCoordinates[j][1] + listOfCoordinates[i][1]) * (listOfCoordinates[j][0] - listOfCoordinates[i][0]))
		j = i
	return(abs(area)/2.0)
	
def readInputs(filename):
	f = open(filename, "r")
	lines = f.read().split("\n")
	result = []
	for line in lines:
		numbers = list(map(int, line.split(",")))
		result.append((numbers[0], numbers[1]))
	return(result)

if __name__ == "__main__":
	
	#################### Part 1 tests
	
	print(gridDistance((0,0),(1,2)) == 3)
	
	testListOfCoordinates = [
		(1, 1),
		(1, 6),
		(8, 3),
		(3, 4),
		(5, 5),
		(8, 9)
	]
	
	print(get2dCoordinatesFurtherstFromOrigin(testListOfCoordinates) == (8,9))
	print(areaOfPolygonIn2dEuclideanSpace([(2,2), (4,10), (9,7), (11,2)]) == 45.5)
	draw2dMapOfSpecifiedPoints(testListOfCoordinates)
	
	#################### Part 2 actual
	input = readInputs("input.txt")
	draw2dMapOfSpecifiedPoints(input) # will need to print this to a csv or something to visualise