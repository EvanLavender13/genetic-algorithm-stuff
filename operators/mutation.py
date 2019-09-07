import numpy as np


def uniform_binary(child, prob):
    size = len(child)

    for i in range(size):
        if np.random.random_sample() < prob:
            child[i] = 1 - child[i]


def uniform_integer(child, low, high, prob):
    size = len(child)

    for i in range(size):
        if np.random.random_sample() < prob:
            child[i] = np.random.random_integers(low, high)
