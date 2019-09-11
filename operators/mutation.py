import random

import numpy as np

import tools


# this one modifies the child in place, whereas the others don't
# is one way preferable to the other?
# hmmmmmmm..........
def single_swap(child):
    i, j = random.sample(range(len(child[1])), 2)

    child[1][i], child[1][j] = child[1][j], child[1][i]

    return child


def uniform(child, prob, func, *args):
    return 0, [func(gene, *args) if tools.prob() < prob else gene for gene in child[1]]


def uniform_binary(child, prob):
    return uniform(child, prob, lambda x: 1 - x)


def uniform_integer(child, low, high, prob):
    return uniform(child, prob, lambda _, x, y: np.random.random_integers(x, y), low, high)
