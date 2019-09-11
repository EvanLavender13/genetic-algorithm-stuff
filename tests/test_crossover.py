import unittest

from operators import crossover


class TestCrossover(unittest.TestCase):

    def test_single_point(self):
        ind1 = [1, 1, 1, 1, 1]
        ind2 = [0, 0, 0, 0, 0]

        child = crossover._single_point(ind1, ind2, 1)
        self.assertEqual(child, [1, 0, 0, 0, 0])
        child = crossover._single_point(ind1, ind2, 2)
        self.assertEqual(child, [1, 1, 0, 0, 0])
        child = crossover._single_point(ind1, ind2, 3)
        self.assertEqual(child, [1, 1, 1, 0, 0])
        child = crossover._single_point(ind1, ind2, 4)
        self.assertEqual(child, [1, 1, 1, 1, 0])

        child = crossover._single_point(ind1, ind2, 0)
        self.assertEqual(len(child), len(ind1))
        child = crossover._single_point(ind1, ind2, 5)
        self.assertEqual(len(child), len(ind1))

    def test_ordered(self):
        ind1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ind2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        child = crossover._ordered(ind1, ind2, 0, 5)
        self.assertEqual(child, [1, 2, 3, 4, 5, 10, 9, 8, 7, 6])
        child = crossover._ordered(ind1, ind2, 5, 10)
        self.assertEqual(child, [5, 4, 3, 2, 1, 6, 7, 8, 9, 10])
        child = crossover._ordered(ind1, ind2, 3, 7)
        self.assertEqual(child, [10, 9, 8, 4, 5, 6, 7, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
