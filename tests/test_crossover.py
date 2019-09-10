import unittest

from operators import crossover


class TestCrossover(unittest.TestCase):

    def test_single_point(self):
        ind1 = [1, 1, 1, 1, 1]
        ind2 = [0, 0, 0, 0, 0]

        child = crossover.single_point(ind1, ind2, p=1)
        self.assertEqual(child, [1, 0, 0, 0, 0])
        child = crossover.single_point(ind1, ind2, p=2)
        self.assertEqual(child, [1, 1, 0, 0, 0])
        child = crossover.single_point(ind1, ind2, p=3)
        self.assertEqual(child, [1, 1, 1, 0, 0])
        child = crossover.single_point(ind1, ind2, p=4)
        self.assertEqual(child, [1, 1, 1, 1, 0])


if __name__ == '__main__':
    unittest.main()
