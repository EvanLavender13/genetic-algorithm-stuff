import numpy as np

import tools


def select_generator(pop, func, *args):
    size = len(pop)
    count = 0

    while count < size:
        count += 1

        yield pop[func(*args)][1], pop[func(*args)][1]


def roulette(population):
    sorted_pop = tools.sort(population, reverse=True)
    total = sum(fit for fit, _ in sorted_pop)
    probs = [fit / total for fit, _ in sorted_pop]
    size = len(sorted_pop)

    return select_generator(sorted_pop, lambda x, y: np.random.choice(x, p=y), size, probs)
