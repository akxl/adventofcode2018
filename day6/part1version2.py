# Advent of Code 2018 Day 5 Part 1 version 1
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