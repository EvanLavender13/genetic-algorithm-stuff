import numpy as np


def binary_list(size):
    return integer_list(size, 0, 1)


def integer_list(size, low, high):
    return 0, list(np.random.random_integers(low, high, size))


def integer_permutation(low, high):
    return 0, list(np.random.permutation(range(low, high + 1)))
