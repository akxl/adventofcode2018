# Advent of Code Day 7 Part 1 Attempt 2
# Author: Aaron Leong

from typing import List, Set, Tuple, Dict
from copy import deepcopy


class Process:
    def __init__(self, name: str, parentProcesses: List[str], childProcesses: List[str]) -> None:
        self.name = name
        self.parentProcesses = parentProcesses
        self.childProcesses = childProcesses

    def getParentProcesses(self) -> List[str]:
        return self.parentProcesses

    def getChildProcesses(self) -> List[str]:
        return self.childProcesses

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __str__(self) -> str:
        return f"Name: {self.name}; Parent processes: {self.parentProcesses}; Child processes: {self.childProcesses}"

    def __repr__(self) -> str:
        return str(self)


class ProcessBuilder:

    def __init__(self, name: str, parentProceses: Set[str], childProcesses: Set[str]) -> None:
        self.name = name
        self.parentProcesses = parentProceses
        self.childProcesses = childProcesses

    def addParentProcess(self, newParentProcess: str) -> None:
        self.parentProcesses.add(newParentProcess)

    def addChildProcess(self, newChildProcess: str) -> None:
        self.childProcesses.add(newChildProcess)

    def build(self) -> Process:
        childProcesses = sorted(list(self.childProcesses))
        parentProcesses = sorted(list(self.parentProcesses))
        return Process(self.name, parentProcesses, childProcesses)

    def __str__(self) -> str:
        return f"Name: {self.name}; Parent processes: {self.parentProcesses}; Child processes: {self.childProcesses};"

    def __repr__(self) -> str:
        return str(self)


def readInputFile(filename: str) -> List[Process]:
    processes: List[Tuple[str, str]] = [(x[5], x[36]) for x in open(filename, "r").read().split("\n")]
    allProcesses: Set[str] = {element for pair in processes for element in pair}
    processesDictionary: Dict[str, ProcessBuilder] = {key: ProcessBuilder(key, set(), set()) for key in allProcesses}

    for process in processes:
        parent, child = process
        processesDictionary[parent].addChildProcess(child)
        processesDictionary[child].addParentProcess(parent)

    return [x.build() for x in processesDictionary.values()]


def findFirsts(processes: List[Process]) -> List[Process]:
    return sorted(list(filter(lambda x: not x.getParentProcesses(), processes)), key=lambda x: x.name)


def findLasts(processes: List[Process]) -> List[Process]:
    return sorted(list(filter(lambda x: not x.getChildProcesses(), processes)), key=lambda x: x.name)


def processProcesses(processes: List[Process]) -> List[str]:
    result: List[str] = []
    workingList: List[Process] = processes
    firsts = findFirsts(processes)

    for x in firsts:
        result.append(x.name)
        workingList.remove(x)

    while len(workingList) > 0:
        workingList = sorted(workingList, key=lambda elem: elem.name)
        for process in workingList:
            if set(process.parentProcesses).issubset(set(result)):
                result.append(process.name)
                workingList.remove(process)
                break

    return list(result)


if __name__ == "__main__":
    testProcesses = readInputFile("sample.txt")
    print(processProcesses(testProcesses) == ["C", "A", "B", "D", "F", "E"])

