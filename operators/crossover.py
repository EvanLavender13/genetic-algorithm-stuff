import random

import numpy as np


def single_point(ind1, ind2):
    size = len(ind1)

    _single_point(ind1, ind2, np.random.randint(1, size - 1))


def _single_point(ind1, ind2, point):
    return list(np.concatenate([ind1[:point], ind2[point:]]))


def ordered(ind1, ind2):
    size = len(ind1)

    i, j = sorted(random.sample(range(size + 1), 2))

    return _ordered(ind1, ind2, i, j)


def _ordered(ind1, ind2, i, j):
    size = len(ind1)

    # get section from first parent
    a = ind1[i:j]

    # fill in remainder from second parent
    b = [k for k in ind2 if k not in a]

    return [a.pop(0) if i <= index < j else b.pop(0) for index in range(0, size)]
