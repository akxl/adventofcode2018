# Advent of Code 2018 Day 7 Part 1
# Author: Aaron

from typing import List

class Process:
    completedParentProcesses = []
    internalCounter = 0

    def __init__(self, name: str, subProcesses: List[str], parentProcesses: List[str]):
        self.name = name
        self.childProcesses = sorted(subProcesses)
        self.parentProcesses = sorted(parentProcesses)
        self.numberOfChildProcesses = len(subProcesses)
        self.numberOfParentProcesses = len(parentProcesses)

    def addChildProcess(self, subProcess: str) -> None:
        self.childProcesses.append(subProcess)
        self.numberOfChildProcesses += 1

    def addParentProcess(self, parentProcess: str) -> None:
        self.parentProcesses.append(parentProcess)
        self.numberOfParentProcesses += 1

    def sneakpeak(self) -> str:
        return self.childProcesses[self.internalCounter]

    def getNextChildProcess(self) -> str:
        if self.internalCounter < self.numberOfChildProcesses:
            nextChild = self.childProcesses[self.internalCounter]
            self.internalCounter += 1
            return nextChild
        else:
            return "You have run out of child processes"

    def flipChildProcesses(self, reattempt: int):
        partone = [self.childProcesses[reattempt]]
        parttwo = self.childProcesses[:reattempt]
        partthree = self.childProcesses[reattempt + 1:]
        self.childProcesses = partone
        self.childProcesses.append(parttwo)
        self.childProcesses.append(partthree)

    def getChildProcesses(self) -> List[str]:
        return sorted(self.childProcesses)

    def getParentProcesses(self) -> List[str]:
        return sorted(self.parentProcesses)

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __str__(self) -> str:
        return f"Name: {self.name}; Parents: {self.parentProcesses}; Children: {self.childProcesses}"


def readAndStoreInputs(filename):
    f = open(filename, "r")
    lines = f.read().split("\n")

    processes = []
    for line in lines:
        parentProcess = line[5]
        childProcess = line[36]

        existingChildProcess = list(filter(lambda process: process.name == childProcess, processes))
        if len(existingChildProcess) == 0:
            processes.append(Process(childProcess, [], [parentProcess]))
        elif len(existingChildProcess) == 1:
            existingChildProcess[0].addParentProcess(parentProcess)
        else:
            raise ValueError("More than one instance of " + childProcess + " is found. Child process branch.")

        existingParentProcess = list(filter(lambda process: process.name == parentProcess, processes))
        if len(existingParentProcess) == 0:
            processes.append(Process(parentProcess, [childProcess], []))
        elif len(existingParentProcess) == 1:
            existingParentProcess[0].addChildProcess(childProcess)
        else:
            raise ValueError("More than one instance of " + parentProcess + " is present. Parent process branch.")

    return(processes) # shit, how do I know what the parent is if it is in a list? I want to just return the parent


def findEnd(processes):
    return list(filter(lambda process: len(process.childProcesses) == 0, processes))


def findStart(processes):
    return list(filter(lambda process: len(process.parentProcesses) == 0, processes))


def orderProcesses(processes: List[Process]) -> List[str]:
    startingProcess: Process = sorted(findStart(processes), key=lambda x: x.name)[0]
    endingProcess: Process = sorted(findEnd(processes), key=lambda  x: x.name)[0]

    properOrder = [startingProcess.name]
    currentProcess = startingProcess
    nextProcessName = startingProcess.sneakpeak()
    print("^^^^^")
    print(nextProcessName)

    i = 0
    while len(properOrder) == 0 or properOrder[-1] != endingProcess.name:
        i = i + 1
        print(i)
        print(properOrder)
        nextProcess = list(filter(lambda x: x.name == nextProcessName, processes))[0]
        print(nextProcess)

        attempt = 0
        if set(nextProcess.getParentProcesses()).issubset(set(properOrder)):
            newCurrentProcessName = currentProcess.getNextChildProcess()
            print("my new current process name")
            print(newCurrentProcessName)
            properOrder.append(newCurrentProcessName)
            currentProcess = list(filter(lambda x: x.name == newCurrentProcessName, processes))[0]
            nextProcessName = currentProcess.sneakpeak()
        else:
            attempt += 1
            currentProcess.flipChildProcesses(attempt)
            nextProcessName = currentProcess.sneakpeak()

    return properOrder





if __name__ == "__main__":
    # testing part 1
    testInput = readAndStoreInputs("sample.txt")
    #for process in testInput:
    #    print(process)

    orderProcesses(testInput)

