import statistics
from operator import itemgetter

import numpy as np


def mean(population):
    return statistics.mean([ind[0] for ind in population])


def sort(population, reverse=False):
    return sorted(population, key=itemgetter(0), reverse=reverse)


def best(population):
    return max(population, key=itemgetter(0))


def prob():
    return np.random.random_sample()
