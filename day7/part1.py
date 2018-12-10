# Advent of Code 2018 Day 7 Part 1
# Author 

class Process:
    completedParentProcesses = []

    def __init__(self, name, subProcesses, parentProcesses):
        self.name = name
        self.subProcesses = subProcesses
        self.parentProcesses = parentProcesses

    def addChildProcess(self, subProcess):
        self.subProcesses.append(subProcess)

    def addParentProcess(self, parentProcess):
        self.parentProcesses.append(parentProcess)

    def __str__(self):
        return f"Name: {self.name}; Parents: {self.parentProcesses}; Children: {self.subProcesses}"


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


if __name__ == "__main__":
    # testing part 1
    testInput = readAndStoreInputs("sample.txt")
    for process in testInput:
        print(process)
