# Advent of Code 2018 Day 5 Part 1
# Author: Aaron Leong

# Aim: I need to find the specified point with the largest number of other points that are closest to it, so long as that number is not infinite.
# My hypothesis is that, for a given Manhatten Grid and specified points, points that lie on the bonundary will have an infinite number of other points in the Grid that are closest to it. My question is then, how to I determine this boundary? So that I can pin point the specified points on the boundary so that I can discount them?
# My guess is that for the general case, I should search for the combinatio of specified points that I can put on the boundary that will give me the largest area.
# Or if I am lazy, I can just precalculate the boundary by hand for this particular exercise, and discount the points on said boundary.
# Note that for this exercise, the 'wall' on x=0 and y=0 are boundaries too, but the specified points on this boundary may or may not result in an infinite number of other points that are closest to said specified points.

def gridDistance(vector1, vector2):
	if (len(vector1) != len(vector2)):
		raise ValueError("vector1 and vector2 must have the same dimension/length")
	length = len(vector1)
	distance = 0
	for i in range(0, length):
		distance += abs(vector1[i] - vector2[i])
	return(distance)

def draw2dMapOfSpecifiedPoints(listOfCoordinates):
	return(1)

if __name__ == "__main__":
	print(gridDistance((0,0),(1,2)) == 3)