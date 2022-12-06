import unittest
from GeneticAlgo import Genetic

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_fitness(self):
        pop = Genetic([1,2,3,2], [64,432,23,1], 3543)
        self.assertEqual(len(pop.weights), len(pop.profits), "Populations not equal")

if __name__ == '__main__':
    unittest.main()
