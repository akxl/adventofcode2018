# Advent of code Day 4 Part 1
# Author: Aaron Leong

from datetime import datetime, timedelta
from copy import deepcopy

def sortAndProcessLog(lines):
	processedLog = []
	for line in sorted(lines):
		year = int(line[1:5])
		month = int(line[6:8])
		day = int(line[9:11])
		hour = int(line[12:14])
		minute = int(line[15:17])
		content = line[19:]
		
		if int(hour) != 23:
			date = datetime(int(year), int(month), int(day))
		else:
			date = datetime(int(year), int(month), int(day)) + timedelta(days=1)
		
		processedLog.append((date, year, month, day, hour, minute, content))
	return(processedLog)

def groupShifts(processedLines):
	shifts = {}
	data = []
	currentDate = datetime(1,1,1)
	for i, line in enumerate(processedLines):
		date, year, month, day, hour, minute, content = line
		if i == 0:
			currentDate = date
		if currentDate == date:
			data.append((year, month, day, hour, minute, content))
		else:
			shifts[currentDate] = deepcopy(data)
			data = []
			currentDate = date
			data.append((year, month, day, hour, minute, content))
	return(shifts)
			
		
		
		
	
if __name__ == "__main__":
	# tests
	testInputArray = [
		"[1518-05-08 00:12] falls asleep",
		"[1518-09-09 00:04] Guard #1543 begins shift",
		"[1518-04-05 00:00] Guard #131 begins shift",
		"[1518-09-12 00:54] falls asleep",
		"[1518-08-28 00:12] falls asleep",
		"[1518-07-08 23:58] Guard #1997 begins shift",
		"[1518-07-09 00:58] wakes up"
	]
	#print(sortAndProcessLog(testInputArray))
	print(groupShifts(sortAndProcessLog(testInputArray)))
	
	# actual
	#f = open("input.txt", "r")
	#inputList = f.read().split("\n")
	#print(groupShifts(sortAndProcessLog(inputList)))