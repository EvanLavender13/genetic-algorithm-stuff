import numpy as np


def binary_list(size):
    return integer_list(0, 2, size)


def integer_list(low, high, size):
    return np.random.randint(low, high, size)
