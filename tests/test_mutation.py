import unittest

from operators import mutation


class TestMutation(unittest.TestCase):

    def test_single_swap(self):
        child = [1, 2, 3, 4, 5]
        mutation._single_swap(child, 0, 1)
        self.assertEqual(child, [2, 1, 3, 4, 5])

        child = [1, 2, 3, 4, 5]
        mutation._single_swap(child, 0, 4)
        self.assertEqual(child, [5, 2, 3, 4, 1])

        child = [1, 2, 3, 4, 5]
        mutation._single_swap(child, 4, 2)
        self.assertEqual(child, [1, 2, 5, 4, 3])

    def test_uniform(self):
        child = [0, 0, 0, 0, 0]

        mutation._uniform(child, 1.0, lambda _: 1)
        self.assertEqual(child, [1, 1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
