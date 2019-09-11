import random

import numpy as np


def single_point(ind1, ind2, p=None):
    size = len(ind1[1])
    point = p if p and 0 < p < size else np.random.randint(1, size - 1)

    return 0, list(np.concatenate([ind1[1][:point], ind2[1][point:]]))


def ordered(ind1, ind2):
    size = len(ind1[1])
    i, j = sorted(random.sample(range(size + 1), 2))

    # get section from first parent
    a = ind1[1][i:j]

    # fill in remainder from second parent
    b = [k for k in ind2[1] if k not in a]

    return 0, [a.pop(0) if i <= index < j else b.pop(0) for index in range(0, size)]
