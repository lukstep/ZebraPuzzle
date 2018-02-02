import unittest
from population import *

class TestPopulation(unittest.TestCase):

    def test_init(self):
        p = population(100)
        self.assertEqual(p.populationSize, 100)

if __name__ == '__main__':
    unittest.main()