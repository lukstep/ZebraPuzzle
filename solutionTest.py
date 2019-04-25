import unittest
from solution import solution

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

    def test_testCorrectSolution(self):
        s = solution()
        s.solution = correctSolution
        self.assertEqual(s.getFitnes(), 100.0)

    def test_testIncorrectSolution(self):
        s = solution()
        s.solution = incorrectSolution
        self.assertEqual(s.getFitnes(), -100.0)

    def test_CheckRule(self):
        s = solution()
        s.solution = correctSolution
        self.assertTrue(s.checkRule('color', 'Yellow', 'nation', 'Norwegian'))

    def test_CheckRule_incorect(self):
        s = solution()
        s.solution = incorrectSolution
        self.assertFalse(s.checkRule('color', 'Yellow', 'drink', 'Coffe'))

    def test_CheckRule2(self):
        s = solution()
        s.solution = correctSolution
        self.assertTrue(s.checkRule2('color', 'Yellow', 'color', 'Blue'))

    def test_CheckRule2_incorect(self):
        s = solution()
        s.solution = incorrectSolution
        self.assertFalse(s.checkRule2('color', 'Yellow', 'color', 'Blue'))

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
