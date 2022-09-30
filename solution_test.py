import unittest
from unittest.mock import MagicMock
from solution import Solution

correctSolution = [{'color': 'Yellow', 'nation': 'Norwegian',  'drink': 'Water',        'smoke': 'Kools',         'pet': 'Fox'},
                   {'color': 'Blue',   'nation': 'Ukrainian',  'drink': 'Tea',          'smoke': 'Chesterfield',  'pet': 'Horse'},
                   {'color': 'Red',    'nation': 'Englishman', 'drink': 'Milk',         'smoke': 'Old Gold',      'pet': 'Snails'},
                   {'color': 'Ivory',  'nation': 'Spaniard',   'drink': 'Orange juice', 'smoke': 'Lucky Strike',  'pet': 'Dog'},
                   {'color': 'Green',  'nation': 'Japanese',   'drink': 'Coffe',        'smoke': 'Parliaments',   'pet': 'Zebra'}]

incorrectSolution = [{'color': 'Ivory',  'nation': 'Spaniard',  'drink': 'Milk',  'smoke': 'Kools',       'pet': 'Horse'},
                     {'color': 'Yellow', 'nation': 'Norwegian', 'drink': 'Water', 'smoke': 'Parliaments', 'pet': 'Fox'},
                     {'color': 'Ivory',  'nation': 'Norwegian', 'drink': 'Water', 'smoke': 'Parliaments', 'pet': 'Fox'},
                     {'color': 'Yellow', 'nation': 'Norwegian', 'drink': 'Milk',  'smoke': 'Parliaments', 'pet': 'Fox'},
                     {'color': 'Ivory',  'nation': 'Norwegian', 'drink': 'Milk',  'smoke': 'Parliaments', 'pet': 'Fox'}]

class TestSolution(unittest.TestCase):
    def test_CorrectSolution(self):
        s = Solution()
        s.solution = correctSolution
        self.assertEqual(s.getFitness(), 100.0)

    def test_IncorrectSolution(self):
        s = Solution()
        s.solution = incorrectSolution
        self.assertEqual(s.getFitness(), -100.0)

    def test_CheckSingleHouseRule(self):
        s = Solution()
        s.solution = correctSolution
        self.assertTrue(s.checkSingleHouseRule('color', 'Yellow', 'nation', 'Norwegian'))

    def test_CheckSingleHouseRule_incorect(self):
        s = Solution()
        s.solution = incorrectSolution
        self.assertFalse(s.checkSingleHouseRule('color', 'Yellow', 'drink', 'Coffe'))

    def test_CheckNeighborhoodRules(self):
        s = Solution()
        s.solution = correctSolution
        self.assertTrue(s.checkNeighborhoodRules('color', 'Yellow', 'color', 'Blue'))

    def test_CheckNeighborhoodRules_incorect(self):
        s = Solution()
        s.solution = incorrectSolution
        self.assertFalse(s.checkNeighborhoodRules('color', 'Yellow', 'color', 'Blue'))

    def test_Reproduce(self):
        solutionA = Solution()
        solutionB = Solution()
        solutionA.solution = solutionB.solution = correctSolution
        reproducedSolution = Solution()
        reproducedSolution.isMutationPossible = MagicMock(return_value=False)
        reproducedSolution(solutionA, solutionB)
        self.assertEqual(reproducedSolution.solution, correctSolution)

    def test_ReproduceNo(self):
        solutionA = Solution()
        solutionB = Solution()
        solutionA.solution = solutionB.solution = correctSolution
        reproducedSolution = Solution()
        reproducedSolution.isMutationPossible = MagicMock(return_value=True)
        reproducedSolution(solutionA, solutionB)
        self.assertTrue(reproducedSolution.solution != correctSolution)

    def test_Mutation(self):
        testSolution = Solution()
        testSolution.solution = correctSolution
        testSolution.mutate()
        self.assertTrue(testSolution.solution == correctSolution)

if __name__ == '__main__':
    unittest.main()
