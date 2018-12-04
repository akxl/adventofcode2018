def makeEncodingMap():
	mapping = {}
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	for index, letter in enumerate(alphabet):
		mapping[letter] = index + 1
	return mapping


def encode(mapping, line):
	result = []
	for x in list(line):
		result.append(mapping[x])
	return(result)
	

def findDifference(mapping, line1, line2):
	result1 = encode(mapping, line1)
	result2 = encode(mapping, line2)
	finalResult = []
	for x in zip(result1, result2):
		finalResult.append(x[0] - x[1])
	numberOfDifferences = 0
	similarLetters = []
	for index, difference in enumerate(finalResult):
		if difference != 0:
			numberOfDifferences += 1
		else:
			similarLetters.append(line1[index])
	if numberOfDifferences == 1:
		return True, numberOfDifferences, similarLetters, line1, line2
	else:
		return False, numberOfDifferences, similarLetters, "", ""

def find(mapping, array):
	targets = array
	for index, line in enumerate(array):
		for target in targets[index:]:
			result = findDifference(mapping, line, target)
			if result[0] == True:
				return(result)
	return False, -1, [], "", ""
				
	
if __name__ == "__main__":
	mapping = makeEncodingMap()
	print(findDifference(mapping, "abcde", "axcye")[0] == False) # expect False
	print(findDifference(mapping, "fghij", "fguij")[0] == True) # expect True
	
	sampleList = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
	print(find(mapping, sampleList)[0] == True)
	
	f = open("input.txt", "r")
	input = f.read().split()
	#print(input)
	print(find(mapping, input))
	
	
	