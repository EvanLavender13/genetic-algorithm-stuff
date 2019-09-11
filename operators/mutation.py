import random

import numpy as np

import tools


def single_swap(child):
    size = len(child)
    i, j = random.sample(range(size), 2)

    child[i], child[j] = child[j], child[i]


def uniform(child, prob, func, *args):
    size = len(child)

    for index in range(size):
        gene = child[index]

        child[index] = func(gene, *args) if tools.prob() < prob else gene


def uniform_binary(child, prob):
    uniform(child, prob, lambda x: 1 - x)


def uniform_integer(child, low, high, prob):
    uniform(child, prob, lambda _, x, y: np.random.random_integers(x, y), low, high)
