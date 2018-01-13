import unittest
from solution import *

correctSolution = [{'color': 'Yellow', 'nation': 'Norwegian', 'drink': 'Water', 'smoke': 'Kools', 'pet': 'Fox'},
                   {'color': 'Blue', 'nation': 'Ukrainian', 'drink': 'Tea', 'smoke': 'Chesterfields', 'pet': 'Horse'},
                   {'color': 'Red', 'nation': 'Englishman', 'drink': 'Milk', 'smoke': 'Old Gold', 'pet': 'Snails'},
                   {'color': 'Ivory', 'nation': 'Spaniard', 'drink': 'Orange juice', 'smoke': 'Lucky Strike', 'pet': 'Dog'},
                   {'color': 'Green', 'nation': 'Japanese', 'drink': 'Coffee', 'smoke': 'Parliaments', 'pet': 'Zebra'}]


class TestSolution(unittest.TestCase):

    def test_live(self):
        s = solution()
        s.solution = correctSolution
        self.assertEqual(s.getFitnes(), 100.0)

    def test_CheckRule(self):
        s = solution()
        s.solution = correctSolution
        self.assertTrue(s.checkRule('color', 'Yellow', 'nation', 'Norwegian'))

    def test_CheckRule2(self):
        s = solution()
        s.solution = correctSolution
        self.assertTrue(s.checkRule2('color', 'Yellow', 'color', 'Blue'))

    def test_Reproduce(self):
        solutionA = solution()
        solutionB = solution()
        solutionA.solution = solutionB.solution = correctSolution
        reproducedSolution = solution()
        reproducedSolution.mutationProbabily = 0
        reproducedSolution.reproduce(solutionA, solutionB)
        self.assertEqual(reproducedSolution.solution, correctSolution)

    def test_ReproduceNo(self):
        solutionA = solution()
        solutionB = solution()
        solutionA.solution = solutionB.solution = correctSolution
        reproducedSolution = solution()
        reproducedSolution.mutationProbabily = 1000
        reproducedSolution.reproduce(solutionA, solutionB)
        self.assertTrue(reproducedSolution.solution != correctSolution)

if __name__ == '__main__':
    unittest.main()
