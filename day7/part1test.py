import unittest
import part1
from part1 import Process

class Part1Test(unittest.TestCase):

    def testReadAndStoreInputs(self):
        testInput = part1.readAndStoreInputs("sample.txt")
        expectedInput = [
            Process("A", ["B", "D"], ["C"]),
            Process("C", ["A", "F"], []),
            Process("F", ["E"], ["C"]),
            Process("B", ["E"], ["A"]),
            Process("D", ["E"], ["A"]),
            Process("E", [], ["B", "D", "F"]),
        ]
        self.assertEqual(testInput, expectedInput)

    def testFindStart(self):
        testInput = part1.readAndStoreInputs("sample.txt")
        expectedOutput = [Process("C", ["A", "F"], [])]
        testOutput = part1.findStart(testInput)
        self.assertEqual(testOutput, expectedOutput)

    def testFindEnd(self):
        testInput = part1.readAndStoreInputs("sample.txt")
        expectedOutput = [Process("E", [], ["B", "D", "F"])]
        testOutput = part1.findEnd(testInput)
        self.assertEqual(testOutput, expectedOutput)