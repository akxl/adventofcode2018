
def pairsAndTriplets(line):
	counter = {}
	keys = list(counter.keys())
	for character in list(line):
		if character in keys:
			counter[character] += 1
		else:
			counter[character] = 1
			keys = list(counter.keys())
	
	pairs, triplets = 0, 0
	for key in counter.keys():
		if counter[key] == 2:
			pairs += 1
		if counter[key] == 3:
			triplets += 1
	
	return pairs, triplets

def checksum(arrayOfStrings):
	pnt = map(pairsAndTriplets, arrayOfStrings)
	pairs = 0
	triplets = 0
	for x in pnt:
		if x[0] > 0:
			pairs += 1
		if x[1] > 0:
			triplets += 1
			
	return(pairs * triplets)
	
if __name__ == "__main__":
	
	# pairsAndTriplets() test
	print(pairsAndTriplets("abcdef") == (0, 0))
	print(pairsAndTriplets("bababc") == (1, 1))
	print(pairsAndTriplets("abbcde") == (1, 0))
	print(pairsAndTriplets("abcccd") == (0, 1))
	print(pairsAndTriplets("aabcdd") == (2, 0))
	print(pairsAndTriplets("abcdee") == (1, 0))
	print(pairsAndTriplets("ababab") == (0, 2))
	
	# checksum() test
	sampleList = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
	print(checksum(sampleList) == 12)
	
	# reading and computing actual checksum
	f = open("input.txt", "r")
	input = f.read().split()
	print(checksum(input)) # answer is 8892
	
	
	
	
	