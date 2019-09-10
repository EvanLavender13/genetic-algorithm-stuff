import numpy as np

import tools


def uniform(child, prob, func, *args):
    return [func(gene, *args) if tools.prob() < prob else gene for gene in child]


def uniform_binary(child, prob):
    return uniform(child, prob, lambda x: 1 - x)


def uniform_integer(child, low, high, prob):
    return uniform(child, prob, lambda _, x, y: np.random.random_integers(x, y), low, high)
