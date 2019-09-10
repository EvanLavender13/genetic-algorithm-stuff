import numpy as np


def single_point(ind1, ind2, p=None):
    size = len(ind1)
    point = p if 0 < p < size else np.random.randint(1, size - 1)

    return list(np.concatenate([ind1[:point], ind2[point:]]))
