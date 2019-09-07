import numpy as np


def single_point(ind1, ind2):
    size = len(ind1)
    point = np.random.randint(1, size - 1)

    return np.concatenate([ind1[:point], ind2[point:]])
