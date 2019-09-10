from operator import itemgetter

import numpy as np


def select_generator(pop, func, *args):
    size = len(pop)
    count = 0

    while count < size:
        count += 1

        yield pop[func(*args)][1], pop[func(*args)][1]


def roulette(population):
    sorted_pop = sorted(population, key=itemgetter(0))
    size = len(sorted_pop)
    total = sum(fit for fit, _ in sorted_pop)
    probs = [fit / total for fit, _ in sorted_pop]

    return select_generator(sorted_pop, lambda x, y: np.random.choice(x, p=y), size, probs)
