import random

import numpy as np

import tools


def single_swap(child):
    size = len(child)
    i, j = random.sample(range(size), 2)

    _single_swap(child, i, j)


def _single_swap(child, i, j):
    child[i], child[j] = child[j], child[i]


def uniform_binary(child, prob):
    _uniform(child, prob, lambda x: 1 - x)


def uniform_integer(child, low, high, prob):
    _uniform(child, prob, lambda _, x, y: np.random.random_integers(x, y), low, high)


def _uniform(child, prob, func, *args):
    size = len(child)

    for index in range(size):
        gene = child[index]

        if tools.prob() < prob:
            child[index] = func(gene, *args)
