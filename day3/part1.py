def getClothCoordinates(leftOffset, topOffset, width, height):
	clothCoordinates = []
	for x in range(leftOffset+1, leftOffset+width+1):
		for y in range(topOffset+1, topOffset+height+1):
			clothCoordinates.append((x, y))
	return clothCoordinates

def readLine(line):
	components = line.split()
	id = components[0]
	offsets = [int(components[2].split(",")[0]), (int(components[2].split(",")[1][:-1]))]
	dimensions = list(map(int, components[3].split("x")))
	return (id, offsets, dimensions)

def getClothUsage(lines):
	clothUsage = {}
	keys = list(clothUsage.keys())
	for line in lines:
		id, offsets, dimensions = readLine(line)
		print(id)
		coordinates = getClothCoordinates(offsets[0], offsets[1], dimensions[0], dimensions[1])
		for coordinatePair in coordinates:
			if coordinatePair in keys:
				clothUsage[coordinatePair] += 1
			else:
				clothUsage[coordinatePair] = 1
				keys = list(clothUsage.keys())
	return(clothUsage)

def getOverlap(dictionary):
	overlaps = 0
	for key in dictionary.keys():
		if dictionary[key] > 1:
			overlaps += 1
	return(overlaps)
		
def getClothUsageV2(lines):
	clothUsage = set()
	overlaps = set()
	for line in lines:
		id, offsets, dimensions = readLine(line)
		print(id)
		coordinates = getClothCoordinates(offsets[0], offsets[1], dimensions[0], dimensions[1])
		for coordinatePair in coordinates:
			if coordinatePair in clothUsage:
				overlaps.add(coordinatePair)
			else:
				clothUsage.add(coordinatePair)
	return(len(overlaps))
	
def getNonOverlap(lines):
	clothUsage = set()
	overlaps = set()
	for line in lines:
		id, offsets, dimensions = readLine(line)
		coordinates = getClothCoordinates(offsets[0], offsets[1], dimensions[0], dimensions[1])
		for coordinatePair in coordinates:
			if coordinatePair in clothUsage:
				overlaps.add(coordinatePair)
			else:
				clothUsage.add(coordinatePair)
	for line in lines:
		id, offsets, dimensions = readLine(line)
		coordinates = getClothCoordinates(offsets[0], offsets[1], dimensions[0], dimensions[1])
		result = checkIfOverlapping(coordinates, overlaps)
		if result == True:
			return("The non overlapping piece is: " + id)
	return("nope")
			

def checkIfOverlapping(coordinates, overlaps):
	for coordinatePair in coordinates:
		if coordinatePair in overlaps:
			return(False)
	return(True)

if __name__ == "__main__":
	print(getClothCoordinates(1, 2, 2, 2) == [(2,3),(2,4),(3,3),(3,4)])
	print(readLine("#123 @ 3,2: 5x4") == ("#123", [3, 2], [5, 4]))
	
	clothUsage = getClothUsage(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"])
	print(getOverlap(clothUsage) == 4)
	print(getClothUsageV2(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]) == 4)
	
	
	print("\n")
	
	
	f = open("input.txt", "r")
	input = f.read().split("\n")
	
	#actualClothUsage = getClothUsage(input)
	#print(getOverlap(actualClothUsage))
	
	print(getClothUsageV2(input)) # part 1: 116491
	print(getNonOverlap(input)) # part 2: #707