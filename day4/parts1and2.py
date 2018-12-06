# Advent of code Day 4 Parts 1 and 2
# Author: Aaron Leong

from datetime import datetime, timedelta
from copy import deepcopy

# Part 1

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
	lastIndex = len(processedLines) - 1
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
		if i == lastIndex:
			shifts[currentDate] = deepcopy(data)
	return(shifts)

def getGuardAndSleepingMinutes(shifts):
	keys = shifts.keys()
	perGuard = {}
	for key in keys:
		guard = ""
		startSleep = 0
		sleepingMinutes = set()
		for i, line in enumerate(shifts[key]):
			year, month, day, hour, minute, content = line
			if i == 0:
				guard = content.split()[1]
			elif content == "falls asleep":
				startSleep = minute
			elif content == "wakes up":
				sleepingMinutes.update(range(startSleep, minute))
				startSleep = 0
		if guard not in list(perGuard.keys()):
			perGuard[guard] = [sleepingMinutes]
		else:
			#oldList = deepcopy(perGuard[guard])
			#perGuard[guard] = oldList.append(sleepingMinutes)
			perGuard[guard].append(sleepingMinutes)
	return(perGuard)
		
def findGuardWithMostSleep(perGuardInfo):
	keys = perGuardInfo.keys()
	worstGuard = ("none", 0)
	for key in keys:
		total = 0
		for set in perGuardInfo[key]:
			total += len(set)
		if total > worstGuard[1]:
			worstGuard = (key, total)
	return(worstGuard)
	
def findMostSleptMinute(perGuardInfo, guardId):
	sleepInfo = perGuardInfo[guardId]
	minuteCount = {}
	for i in range(0, 61):
		minuteCount[i] = 0
	for set in sleepInfo:
		for minute in list(set):
			minuteCount[minute] += 1
	mostSleptMinute = -1
	mostSleptMinuteCount = -1
	for minute in minuteCount.keys():
		if minuteCount[minute] > mostSleptMinuteCount:
			mostSleptMinute = minute
			mostSleptMinuteCount = minuteCount[minute]
	return(mostSleptMinute, mostSleptMinuteCount)


# Part 2

def countFrequencyPerGuard(perGuardInfo):
	guards = perGuardInfo.keys()
	frequencyTablePerGuard = {}
	for guard in guards:
		frequencyTable = {}
		for minute in range(0, 61):
			frequencyTable[minute] = 0
		for setOfMinutesAsleep in perGuardInfo[guard]:
			for minute in list(setOfMinutesAsleep):
				frequencyTable[minute] += 1
		frequencyTablePerGuard[guard] = frequencyTable
	return(frequencyTablePerGuard)

def getWorstGuardByStrategy2(perGuardInfo):
	guards = perGuardInfo.keys()
	worstGuard = ("none", -1, -1) # guard, minute, frequency
	for guard in guards:
		for minute in range(0, 61):
			if perGuardInfo[guard][minute] > worstGuard[2]:
				worstGuard = (guard, minute, perGuardInfo[guard][minute])
	return(worstGuard)
	
if __name__ == "__main__":
	############# Part 1 tests
	testInputArray = [
		"[1518-05-08 00:12] falls asleep",
		"[1518-09-09 00:04] Guard #1543 begins shift",
		"[1518-04-05 00:00] Guard #131 begins shift",
		"[1518-09-12 00:54] falls asleep",
		"[1518-08-28 00:12] falls asleep",
		"[1518-07-08 23:58] Guard #1997 begins shift",
		"[1518-07-09 00:58] wakes up"
	]
	
	testInputArray2 = [
	"[1518-11-01 00:00] Guard #10 begins shift",
	"[1518-11-01 00:05] falls asleep",
	"[1518-11-01 00:25] wakes up",
	"[1518-11-01 00:30] falls asleep",
	"[1518-11-01 00:55] wakes up",
	"[1518-11-01 23:58] Guard #99 begins shift",
	"[1518-11-02 00:40] falls asleep",
	"[1518-11-02 00:50] wakes up",
	"[1518-11-03 00:05] Guard #10 begins shift",
	"[1518-11-03 00:24] falls asleep",
	"[1518-11-03 00:29] wakes up",
	"[1518-11-04 00:02] Guard #99 begins shift",
	"[1518-11-04 00:36] falls asleep",
	"[1518-11-04 00:46] wakes up",
	"[1518-11-05 00:03] Guard #99 begins shift",
	"[1518-11-05 00:45] falls asleep",
	"[1518-11-05 00:55] wakes up"
	]

	print("Part 1 tests")
	testPerGuardInfo = getGuardAndSleepingMinutes(groupShifts(sortAndProcessLog(testInputArray2)))
	
	print(findGuardWithMostSleep(testPerGuardInfo) == ("#10", 50)) 	# expect 50 minutes of sleep by guard 10
	print(findMostSleptMinute(testPerGuardInfo, "#10") == (24, 2)) # expect 24th minute at 2 times
	
	
	############# Part 1 actual
	print("Part 1 actual")
	f = open("input.txt", "r")
	inputList = f.read().split("\n")
	perGuardInfo = getGuardAndSleepingMinutes(groupShifts(sortAndProcessLog(inputList)))
	worstGuard = findGuardWithMostSleep(perGuardInfo) # ("#2351", 451)
	print(worstGuard)
	print(findMostSleptMinute(perGuardInfo, worstGuard[0])) # (40, 13)
	
	
	
	############# Part 2 test
	print("Part 2 tests")
	print(getWorstGuardByStrategy2(countFrequencyPerGuard(testPerGuardInfo)) == ("#99", 45, 3)) # expect guard 99, who slept on the 45th minute for a total of 3 times
	
	############# Part 2 actual
	print("Part 2 actual")
	print(getWorstGuardByStrategy2(countFrequencyPerGuard(perGuardInfo)))