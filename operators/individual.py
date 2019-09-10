import numpy as np


def binary_list(size):
    return integer_list(0, 1, size)


def integer_list(low, high, size):
    return list(np.random.random_integers(low, high, size))
